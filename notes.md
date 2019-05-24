# General notes
Workflows are characterized by a set of **task** and **asset** definitions.

## Task Specification
Workflow tasks are described in several parts. The current/initial descriptions are independent of CMB-specific items.
1. Objective: a one-sentence description of what the task is for.
2. Input assets: a list of assets that are needed to carry out the task.
3. Output assets: a list of assets that are produced or modified by the task.
4. Software: a list of software tools needed to carry out the task. To start, this will be mainly modelbuilder and some commandline programs or scripts.
5. Description: additional narrative that further describes the task or how to perform it. (Perhaps this section would be better called "info" or "help" )

## The words "Specify" and "Generate"
Current plan is to use either "specify" or "generate" when naming tasks.

* "Specify" implies activities that primarily involve human interaction. An example of this is creating and editing attributes using the CMB user interface.
* "Generate" implies activities that primarily involve computational resources. An example of this is meshing; although a user invokes the mesher, and possibly provides some top-level settings, the contents of the mesh resource are populated by meshing software.
