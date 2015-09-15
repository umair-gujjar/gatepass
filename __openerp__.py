{
    "name": "Task Time Tracking",
    "version": "0.1",
    "author": "Ehtisham Faisal",
    "category": "apps",
    "description":
        """
        This module add an history of the time updates applied on project's tasks.
        
        The thing is, I created this module before stumbling upon project.task.history
        objects, which seems to implement more or less the same features as the
        current module 
        """,
    "summary": "Track time updates on project's tasks.",
    "depends": ["project"],
    "data": [
        # Data & configuration
        "security/ir.model.access.csv",
        # Wizards
        'wizard/remaining_time_view.xml',
        # Views
        'task_view.xml',
    ],
    "demo": [],
    "test": [],
    "auto_install": False,
    "installable": True,
    "application": True,
}
