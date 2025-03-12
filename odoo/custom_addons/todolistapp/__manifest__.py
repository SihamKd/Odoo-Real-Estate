{
    'name': "To Do List App",
    'author': "Siham Khaddou",
    'version': '17.0.0.1.0',
    'category': 'Productivity',
    'depends': ['base', 'mail'],
    'license': 'LGPL-3',
    'summary': 'Manage your tasks efficiently',
    'description': """
        Todo List Application for managing tasks:
        - Create and track tasks
        - Assign to users
        - Set deadlines
        - Mark completion status
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
        'views/todo_base_menu.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # '/todolistapp/static/src/css/property.css'
        ],
    },
    'application': True,
}