import project
import workflow

wf = workflow.create('neams.1')
print('Created workflow:  {}'.format(wf))

project = project.Project(wf)
print('Created project: {}'.format(project))

tasks = project.tasks()
for t in tasks:
    print('Task {}.  {}'.format(t.id, t.title))

project_assocs = project.assets()
for a in project_assocs:
    print('Asset {}.  {}, {}, {}'.format(a.asset.id, a.role, a.pc, a.asset.asset_type))

print()
for t in tasks:
    print('Task {}. {}'.format(t.id, t.title))
    for a in t.assets:
        asset = a.workflow_asset
        print('  Asset {} - {}'.format(asset.role, a.task_pc))

# List task and status/state
# Add asset(s) to project
# List task and status/state
# ?Also remove asset from project?
