collective.schedule
===================

This package integrates the python 'schedule' library (https://github.com/dbader/schedule) with Plone.

It provides the following:

 * A ZML interface for scheduling jobs
 * A single 'tick' job processing view that can be registered using a Zope Clock Server

Configuration
-------------

First add `collective.schedule` to your buildout eggs.
Then register the collective.schedule 'tick' method as a clock server in your buildout config:

    [buildout]
    ...

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zope-conf-additional =
        <clock-server>
          method /plonesitename/@@schedule-tick
          # If you have virtual host rewriting, you will need to
          # use the following format instead:
          # method /VirtualHostBase/http/www.mysite.com/plonesitename/VirtualHostRoot/@@schedule-tick
          period 300
          user username
          password password
        </clock-server>

Scheduling jobs
---------------

You can then register jobs using ZCML as follows:

    <configure
        xmlns:schedule="http://namespaces.zope.org/schedule">

        <include package="collective.schedule" />

        <schedule:job
          view="@@some-regular-job"
          unit="day"
          at="22:00"
          />

    </configure>

Where 'view' is the *name* of a browser view that can be looked up on the Plone Site and executed with the user defined in the clock server above.

For more details on the options for scheduling jobs, see https://github.com/dbader/schedule
