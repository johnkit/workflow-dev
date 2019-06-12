import project
import workflow

from tabulate import tabulate

wf = workflow.create('neams.1')
print('Created workflow:  {}'.format(wf))

project = project.Project(wf)
print('Initialized project to that workflow')

print()
print('Workflow Tasks:')
task_headers = ['Task Id', 'Title', 'Description']
task_table = [[t.id, t.title, t.description] for t in project.tasks()]
print(tabulate(task_table, headers=task_headers))

print()
print('Workflow Assets:')
asset_headers = ['Asset Id', 'Role', 'P/C', 'Type', 'Description']
asset_table = [[a.id, project.role(a), project.pc(a), a.asset_type, a.description] \
    for a in project.assets()]
print(tabulate(asset_table, headers=asset_headers))

print()
print('Workflow Summary')
summary_headers = ['Task Id', 'Asset Id', 'Role', 'P/C', 'Type']
summary_table = None
for t in project.tasks():
    if summary_table is None:
        summary_table = [[t.id, a.id, project.role(a), t.pc(a), a.asset_type] for a in t.assets]
    else:
        summary_table.append([])
        summary_table += [[t.id, a.id, project.role(a), t.pc(a), a.asset_type] for a in t.assets]
print(tabulate(summary_table, headers=summary_headers))
print()

# List task and status/state
# Add asset(s) to project
# List task and status/state
# ?Also remove asset from project?
