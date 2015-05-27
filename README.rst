==============
Events, by Valuehorizon
==============

.. image:: https://travis-ci.org/Valuehorizon/valuehorizon-events.svg?branch=master
   :target: https://travis-ci.org/Valuehorizon/valuehorizon-events
.. image:: https://coveralls.io/repos/Valuehorizon/valuehorizon-events/badge.svg
   :target: https://coveralls.io/r/Valuehorizon/valuehorizon-events
.. image:: https://codeclimate.com/github/Valuehorizon/valuehorizon-events/badges/gpa.svg
   :target: https://codeclimate.com/github/Valuehorizon/valuehorizon-events

A Django-based Foreign Exchange data toolkit. It provides time-series functionality
with built-in statistical plugins such as volatility and returns. You can also write 
your own statistical plugins.
It also includes documentation, test coverage and a good amount of sample data to play around with.
This app is a part of the Valuehorizon application ecosystem.

Installation
============

Start by creating a new ``virtualenv`` for your project ::

    mkvirtualenv myproject

Next install ``numpy`` and ``pandas`` and optionally ``scipy`` ::

    pip install numpy==1.8.0
    pip install scipy==0.13.3
    pip install pandas==0.13.0

Finally, install ``valuehorizon-events`` using ``pip``::

    pip install valuehorizon-events

Contributing
============

Please file bugs and send pull requests to the `GitHub repository`_ and `issue
tracker`_.

.. _GitHub repository: https://github.com/Valuehorizon/valuehorizon-events/
.. _issue tracker: https://github.com/Valuehorizon/valuehorizon-events/issues

Commercial Support
==================

This project is sponsored by Valuehorizon_. If you require assistance on
your project(s), please contact us: support@valuehorizon.com.

.. _Valuehorizon: http://www.valuehorizon.com