from openerp.osv import fields
from openerp.osv.osv import osv, except_osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp


class Task(osv):
    _inherit = 'project.task'

    def _get_time_tracking_line(self, cr, uid, ids, field_name, arg, context=None):
        if context is None:
            context = {}
        result = {}
        for task in self.browse(cr, uid, ids, context=context):
            lines = [l for l in task.time_tracking_line_ids if not l.archived]
            result[task.id] = lines and lines[0] or False
        return result

    _columns = {
      'time_tracking_line_ids': fields.one2many('project.task.tracking_line', 'task_id', string='Time Tracking Lines', readonly=True, help="Time tracking."),
    }

    def _check_active_time_tracking_lines(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        for task in self.browse(cr, uid, ids, context):
            active_lines = [l for l in task.time_tracking_line_ids if not l.archived]
            if len(active_lines) > 1:
                return False
        return True

    _constraints = [
        (_check_active_time_tracking_lines, "No more than one active time tracking line is allowed.", ['time_tracking_line_ids']),
    ]

    def _force_remaining_hours_update(self, cr, uid, ids, vals, context=None):
        """
        When planned time is updated alone, without a remaning time, we have to
        manually set the latter as if it was called by onchange_planned().
        This is required to restore the legacy behaviour we bypassed when we
        forced the remaining_hours field to be read-only (see:
        https://github.com/Smile-SA/smile_openerp_addons_7.0/commit/bfc6f12bfcd89a6e47b4a5dab27622152eac2243#L4R14 ).
        """
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        if 'planned_hours' in vals and 'remaining_hours' not in vals:
            local_context = context.copy()
            local_context.update({'bypass_time_tracking_history': True})
            planned = vals.get('planned_hours', None)
            effective = vals.get('effective_hours', None)
            for task_id in ids:
                if effective is None:
                    effective = self.read(cr, uid, task_id, ['effective_hours'], context=local_context)['effective_hours']
                new_vals = self.onchange_planned(cr, uid, ids, planned, effective)['value']
                self.write(cr, uid, task_id, new_vals, context=local_context)
        return

    def _update_history(self, cr, uid, ids, vals=None, context=None):
        if vals is None:
            vals = {}
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        if context.get('bypass_time_tracking_history', None):
            return
        get_field_value = lambda f: vals.get(f, context.get('default_%s' % f, None))
        planned_time = get_field_value('planned_hours')
        effective_time = get_field_value('effective_hours')
        remaining_time = get_field_value('remaining_hours')
        for task_id in ids:
            line_obj = self.pool.get('project.task.tracking_line')
            # Get current value for the ones not part of the current update
            if None in [planned_time, effective_time, remaining_time]:
                task = self.browse(cr, uid, task_id, context=context)
                if planned_time is None:
                    planned_time = task.planned_hours
                if effective_time is None:
                    effective_time = task.effective_hours
                if remaining_time is None:
                    remaining_time = task.remaining_hours
            # Archive all active tracking lines
            active_line_ids = line_obj.search(cr, uid, [('task_id', '=', task_id), ('archived', '=', False)], context=context)
            line_obj.write(cr, uid, active_line_ids, {'archived': True}, context=context)
            # Add a new tracking time line
            line_obj.create(cr, uid, {'task_id': task_id, 'planned_time': planned_time, 'effective_time': effective_time, 'remaining_time': remaining_time}, context=context)
        return

    def _detect_updates_on(self, field_names, vals=None, context=None):
        """
        Utility method which returns True if one of the provided field is being updated.
        """
        assert isinstance(field_names, (list, tuple))
        if vals is None:
            vals = {}
        if context is None:
            context = {}
        for f in field_names:
            if vals.get(f, context.get('default_%s' % f, None)) != None:
                return True
        return False

    def _track_time_changes(self, cr, uid, ids, vals=None, context=None):
        """
        Catch every update on the legacy remaining_hours and update the history to keep track on changes.
        """
        # List of time-dependent columns of project.task objects
        FIELD_NAMES = ['planned_hours', 'effective_hours', 'remaining_hours', 'work_ids', 'state']
        if self._detect_updates_on(FIELD_NAMES, vals, context):
            self._update_history(cr, uid, ids, vals, context)
        return

    def create(self, cr, uid, vals, context=None):
        ids = super(Task, self).create(cr, uid, vals, context=context)
        self._force_remaining_hours_update(cr, uid, ids, vals, context)
        self._track_time_changes(cr, uid, ids, vals, context)
        return ids

    def write(self, cr, uid, ids, vals, context=None):
        res = super(Task, self).write(cr, uid, ids, vals, context=context)
        self._force_remaining_hours_update(cr, uid, ids, vals, context)
        self._track_time_changes(cr, uid, ids, vals, context)
        return res


class TrackingLine(osv):
    _name = 'project.task.tracking_line'
    _order = "archived asc, write_date desc"

    _columns = {
      'task_id': fields.many2one('project.task', 'Task', readonly=True, required=True, ondelete='cascade', help="Task this time tracking line is attached to."),
      'planned_time': fields.float('Initially Planned Time', readonly=True, required=True, help='Estimated time to do the task, usually set by the project manager when the task is in draft state.'),
      'effective_time': fields.float('Time Spent', readonly=True, required=True, help="Computed using the sum of the task work done."),
      'remaining_time': fields.float('Remaining Time', digits=(16,2), readonly=True, required=True, help="Total remaining time of the task."),
      'write_date': fields.datetime("Modification Date", readonly=True, required=True, help="Last date when the remaining time line was updated."),
      'create_uid':  fields.many2one('res.users', 'Author', readonly=True, required=True, help="The user who changed the time tracking values."),
      'archived': fields.boolean('Archived', readonly=True, help="Flag a time tracking line as archived."),
    }

    _defaults = {
        'archived': False,
    }
