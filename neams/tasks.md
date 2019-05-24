# NEAMS Simulation Workflow - Strawman Tasks
This page outlines the tasks and assets associated with a strawman nuclear simulation.

----
## Specify Geometry
**Objective**: produce the reactor core geometry for simulation.

**Input assets**: none

**Output assets**:
* reactor core model (smtk::session::rgg::Resource)

**Software**
* RGG plugin (generate_mesh.py?)
* MeshKit (library?)
* Cubit (application?)

**Description**:

There are several ways to carry out this task.

* Create RGG model interactively in modelbuilder, manually defining its geometry (pins, ducts, assemblies, core).
* Import .rxf file into modelbuilder.
* Modify the TestModel.h file (?) in RGG session, defining the geomerty to be generated when the program (?) is built and run.


----
## Generate Mesh
**Objective**: produce the "analysis mesh" (discretization) for the simulation.

**Input assets**:
* reactor core model (smtk::session::rgg::Resource)

**Output assets**:
* reactor core mesh (smtk::mesh::Resource)

**Description:**

Generating an analysis mesh involves several steps, but are lumped together here for convenience. There is an "GenerateMesh" operator in the RGG plugin that appears to encapsulate all of the steps.

Can the RGG plugin include a menu item to run the GenerateMesh operator? Or should we produce a command line program to run it?

----
## Specify Simulation Attributes
Note: this task should probably be broken into multiple tasks corresponding to the different simulation codes (NEAMS, Proteus, etc.)

**Objective**: produce the attributes specifying the simulation.

**Input assets**:
* reactor core model (smtk::session::rgg::Resource)

**Output assets**:
* attribute resource (smtk::attribute::Resource)

**Software**:
* modelbuilder
  * RGG plugin (neutroncis workflow files)

**Description**:
The standard CMB attribute interaction.

----
## Generate Simulation Input Files
Note: this task should probably be broken into multiple tasks corresponding to the different simulation codes (NEAMS, Proteus, etc.)

**Objective**: produce the input files needed to submit simulation job.

**Input assets**:
* reactor core model (smtk::session::rgg::Resource)
* simulation attributes (smtk::attribute::Resource)

**Output assets**:
* input files (folder?)

**Software**:
* modelbuilder
  * RGG plugin (neutroncis workflow files)

**Description**:
Run the export operator.
