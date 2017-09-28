# About SPARKL
The SPARKL Sequencing Engine is a rules/execution engine written in Erlang. It can manage the behaviour of distributed machines, systems and applications using an XML-based declarative language. 

It is designed to work with legacy and external systems integrating with just about any application, system or language.

SPARKL comes with a CLI and a GUI, where you can build, execute, test and monitor your processes.

# Documentation 
Documentation for the SPARKL Sequencing Engine can be found online on the [SPARKL docs site](http://docs.sparkl.com/). 

[![Join the chat at https://gitter.im/sparkl/support](https://badges.gitter.im/sparkl/cli.svg)](https://gitter.im/sparkl/support?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Examples & Tutorials <a name="ex_tut"></a>
## To use an example <a name="use_examples"></a>:
1. Save it to your local file system as an `xml` file.
> See shortcut [below](#bulk-importing-all-example-configurations) on how to import **all** example configurations in one go.
2. Open the SPARKL Developer Console
   * You can use a [public instance of the Developer Console](https://saas.sparkl.com)
   > The public instance of the Developer Console is relaunched once or twice per week.
   > As a relaunch removes all registered users and their resources, we recommend backing up your stuff.
   > For example, if you keep your stuff in the `Scratch` folder, you can download the whole folder to your file system.
3. Log into an existing account or create a new one
   * To create a new account: 
     1. Click **Create a New Account**
     2. Enter your e-mail address
     3. Enter your chosen password twice
     4. Try not to forget it
4. Import the `xml` file
   > If you have access to the SPARKL command line interface, use the `Examples/importXmp.sh` script to import all the downloaded configurations to the Developer Console.
5. Run it in the Developer Console
  
## To use a tutorial <a name="use_tutorial"></a>:
 1. Open the SPARKL Developer Console
 2. Create a new folder
 3. Build the mix in the [Editor](http://docs.sparkl.com/#TopicRoot/Editor/the_editor_c.html) with the help of our video guides
 
 ## Bulk importing all example configurations
 ### Dependencies
 * Python 2.7 - get it from [here](https://www.python.org/downloads/ "Python download")
 * Git - get it from [here](https://git-scm.com/downloads)
 * The SPARKL CLI - get it from [here](https://github.com/sparkl/cli/releases)
 * An existing SPARKL user account
 > You can create your user account on the [public instance of the Developer Console](https://saas.sparkl.com)
### Procedure
1. Clone the `examples` repository.
  ```
  $ git clone https://github.com/sparkl/examples.git
  ```
2. From the `python_scripts` directory run the `bulk_import.py` script.
  ```
  $ cd examples/python_scripts
  $ python bulk_import.py
  ```
3. Follow the instructions on the terminal screen. 
> If you choose **not** to import all examples, the script offers them one by one for importing.
  ```
  Enter your SPARKL instance URL: https://saas.sparkl.com
  Connected to https://saas.sparkl.com using alias this_import_alias
  Enter your username: miklos@sparkl.com
  Password: **************
  Logged in as miklos@sparkl.com
  Import all examples? y/n y
  ```
All the selected SPARKL example configurations are imported to your user tree at the specified SPARKL instance. The script also creates the `Scratch` and `Lib` folders in your SPARKL user tree if they are not already there.
> See [this readme](https://github.com/sparkl/examples/tree/master/Library) on the library configurations saved under the `Lib` folder.
