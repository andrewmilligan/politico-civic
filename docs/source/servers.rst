Servers
-------

Civic provides a cli called ``onespot`` that handles server management
for you. 

To get it installed on your path, make sure your virtual
environment is activated, and run ``python setup.py develop``.

**IMPORTANT**: Each ``onespot`` command takes a ``--target=production``
argument in order to make these commands run on the production server.
By default, the commands go to staging.

You will also need to ensure that you have environment files for the
servers in your project. These are gitignored because they contain API
keys that we cannot leak to the public. In both the
``terraform/staging`` and ``terraform/production`` folders, you will
need both a ``.env`` file and a ``terraform.tfvars`` file. Talk to Tyler
if you don’t have these.

You can always run ``onespot help`` for information on the command line.

Provisioning
^^^^^^^^^^^^

Run these commands when you need to create new servers or push new code
to the servers.

Destroy server
''''''''''''''

``onespot server destroy``

This command will completely remove the server and its corresponding security groups from AWS.

Provision new server
''''''''''''''''''''

``onespot server launch``

This command will create a new EC2 instance according to the size defined in `terraform.tfvars`, and associate it with the elastic IP defined in `terraform.tfvars`.

Setup new server
''''''''''''''''

``onespot server setup``

This command will install an SSL certificate, setup logging, and install your nginx and uwsgi configuration files to an existing server. Run this after you have launched a new server.

Updating existing server
''''''''''''''''''''''''

``onespot server update``

This command will grab the latest from the master branch of this repo on Github and put it on the server. Then, it will reinstall requirements, migrate the database if necessary, and collect static files.
