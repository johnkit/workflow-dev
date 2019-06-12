import project
import workflow

wf = workflow.create('neams.1')
print('Created workflow:  {}'.format(wf))

project = project.Project(wf)
print('Created project: {}'.format(project))

for t in project.tasks():
    print('Task {}.  {}'.format(t.id, t.title))

for a in project.assets():
    role = project.role(a)
    pc = project.pc(a)
    print('Asset {}.  {}, {}, {}'.format(a.id, role, pc, a.asset_type))

print()
for t in project.tasks():
    print('Task {}. {}'.format(t.id, t.title))
    for a in t.assets:
        print('  Asset {} - {}'.format(project.role(a), t.pc(a)))

# List task and status/state
# Add asset(s) to project
# List task and status/state
# ?Also remove asset from project?
