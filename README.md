PyFOS - 1.0
=======

### What is PyFOS ###

    PyFOS is a python language binding that works with REST API
    supported in FOS 8.2.0 and up. PyFOS distribution is meant
    1) to provide 1-to-1 functional coverage of FOS REST API and
    2) to provide utility scripts that can be used to directly or
    be used as reference examples to create your own. pyfos/pyfos
    directory contains modules & functions that provides 1-to-1
    functional coverage of FOS REST API. pyfos/pyfos/utils directory
    contains modules & scripts that can be used to kick start
    day-to-day operations or to be used as reference examples for
    your own scripts.

### What can I do with PyFOS? ###

	Since PyFOS provides 1-to-1 functional coverage of underlying
    FOS REST API, all features and functions available through FOS
    REST API is available through PyFOS. Some examples of these are,
    not limited to, port configuration update/get, port statistics
    get/clear, full zoning database management support, NS/fdmi get,
    etc. Please refer to FOS REST API for the full list of features
    and functions.

### FOS and PyFOS versions ###

    PyFOS 1.0 covers up to FOS 8.2.0b

### Directory structure ###

    pyfos - root directory
        \_ pyfos - directory that contains library modules
            \_ utils - directory that contains utility scripts
        \_ docs - directory that contains PyFOS documentations
            \_ documentations
                \_ html - directory that contains Sphinx generated
                            *.html documentations.

### Supported platforms ###

    Tested with Python3 (3.5.2) with setuptools
    Ubuntu 16.04.3 LTS

### Installation ###

    1) create library directories
    mkdir ~<login>/python_lib
    mkdir ~<login>/python_lib/lib
    mkdir ~<login>/python_lib/lib/python3.5
    mkdir ~<login>/python_lib/lib/python3.5/site-packages

    2) set env variable for library directory according to your shell env

        for example for csh:

            setenv PYTHONPATH ~<login>/python_lib/lib/python3.5/site-packages

    3) install dependencies
        pip3 install xmltodict --prefix=~<login>/python_lib
        pip3 install requests --prefix=~<login>/python_lib
        pip3 install jsondiff --prefix=~<login>/python_lib
        pip3 install xlrd --prefix=~<login>/python_lib
        pip3 install colorconsole --prefix=~<login>/python_lib

    4) install pyfos modules into the library path
    cd <pyfos directory>
    python3 setup.py install --prefix=~<login>/python_lib

### HTML based documentation ###

    HTML files are created under <pyfos directory>/docs/documentations/html. use index.html
    as the starting point.

### Uninstall ###

    if library path is used for pyfos & dependencies only - remove the directory as a whole
    if library path is used by other modules also - remove pyfos & dependencies manually

### Contact ###

    Automation.BSN@broadcom.com

### Code walk through of switch_show.py & switch_name_set.py ###

    Before you can make use of the PyFOS modules, you need to import
    them.

        import pyfos.pyfos_auth as pyfos_auth
        import pyfos.pyfos_brocade_fibrechannel_switch as pyfos_switch
        import pyfos.pyfos_util as pyfos_util
        import pyfos.utils.brcd_util as brcd_util

    pyfos_auth module contains login/logout functions.
    pyfos_brocade_fibrechannel_switch module contains switch object
    definition. pyfos_util module contains various utility functions,
    including object print function. utils.brcd_util contains
    primarily script options/inputs handling functions.
    
    We are now ready to login to FOS switch.

        valid_options = []
        inputs = brcd_util.generic_input(argv, usage, valid_options)

        session = pyfos_auth.login(inputs["login"], inputs["password"],
                               inputs["ipaddr"], inputs["secured"],
                               verbose=inputs["verbose"])
        if pyfos_auth.is_failed_login(session):
            print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])
            usage()
            sys.exit()

    Above example uses brcd_util.generic_input() functionn to retrieve
    user inputs in uniform way. The core of what the code segment is
    doing is pyfos_auth.login() function.
    
    Here, you are providing the login name, password associated with
    the login, IP address of the FOS switch to connect to and indication
    to use HTTP or HTTPS. Once successful, a session is returned. This
    dictionary structure contains information in regards to the
    connection to the FOS switch now established. All subsequent
    operations to get/create/update/delete/logout must specify a valid
    and active session.

    Number of concurrent active sessions allowed is controlled based
    on FOS switch configuration. 

    Once you have a session established, we are now ready to get switch
    object to display.
    
        switch = pyfos_switch.fibrechannel_switch.get(session)
        pyfos_util.response_print(switch)
    
    Above example shows how to "get" object from FOS. If getting
    information from FOS is needed, you would want to use get()
    function available from PyFOS object class.

    What the get() function returns can be error code, an object or
    a list of objects. You can check to see if the function returned
    an error by pyfos_util.is_failed_resp(<returned by get>).
    If not an error, you can check to see if the get() returned
    an object or a list of objects by isinstance(<returned by get>, list).

    Although we return an object or a list of objects, you can print
    the object into JSON formatted output by simply print() or
    pyfos_util.response_print().

    You can also "peek" into a specific attribute within the object.
    The function name is "peek_" + name of the attribute with "-"
    converted to "_". So, you can read the "name" of the switch object
    by doing switch.peek_name() after the object has been retrieved
    from FOS using the get() function. An example of above can be
    changed to

        switch = pyfos_switch.fibrechannel_switch.get(session)
        print(port.peek_name())

    When wanting to create/update/delete, you would want to use post(),
    patch() or delete() function provided by the object. Typically,
    you would instantiate an object, set attributes such as key
    and desired attributes for change, and post/patch/delete.

        current_switch = pyfos_switch.fibrechannel_switch.get(session)

        switch = pyfos_switch.fibrechannel_switch()
        name = current_switch.peek_name()
        switch.set_name(name)
        switch.set_user_friendly_name(username)
        result = switch.patch(session)
        pyfos_util.response_print(result)

    In the example above, switch object is first gotten to retrieve
    the name of the switch to be used during patch(). A new switch
    object is instantiated, set WWN in name attribute, set the switch
    name in string, and patch() to apply the change to FOS.

    A single session can be used many times to get/create/update/delete.
    Once all the work is completed, pyfos_auth.logout(<session structure>)
    is called to clear the connection established with the FOS switch.
    Here is what it looks like:

        pyfos_auth.logout(session)


### Contributing ###

    Contributions to this project require the submission of a Contributor Assignment
    Agreement ("CAA"). The CAA transfers the copyright to your contribution from you 
    (or your employer) to Broadcom, and in return Broadcom grants back a license to use 
    your Contribution. This ensures Broadcom has the flexibility to license the 
    project under an appropriate license. 

    Contributor Assignment Agreement ("CAA")
    Contributors must sign and submit a CAA before a contribution can be accepted. Two CAAs are available, one for individual contributions and one for contributions made on behalf of an entity, e.g., an employer. Select the appropriate link below to electronically execute a CAA:
    CAA - Individual:  https://na3.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=7af19c0f-ae97-4b56-b950-fc4796860c79
    CAA - Entity:  https://na3.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=f657df18-ed64-4c51-a8f2-618bbd17d355
                
    For more information on contributing, see CONTRIBUTING.md.
