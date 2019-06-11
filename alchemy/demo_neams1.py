import project
import workflow

wf = workflow.create('neams.1')
print('Created workflow:  {}'.format(wf))

project = project.Project(wf)
print('Created project: {}'.format(project))

tasks = project.tasks()
for t in tasks:
    print('{}.  {}'.format(t.id, t.title))

assocs = project.assets()
for a in assocs:
    print('{}.  {}, {}, {}'.format(a.asset.id, a.role, a.pc, a.asset.asset_type))
