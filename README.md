# OJS API

> Python/Django API for OJS.

## Project

This project is a tool for
* OJS instance :
    * to **expose** its Journals metadata and files through an API accessible to any service registered
    * to **register** these distant consumer services to grant them access to the API
* consumer service :
    * to **retrieve** Journals metadata and files from any OJS instance where it is registered

## OJS versions supported

* 2.4.8

## Installation

## OJS instance usage

An OJS instance may choose to expose its Journals metadata and files to a registered distant consumer service. To do so, it has to
* install this tool (see previous section)
* expose API
* register services

### Expose API

### Register a service

## Consumer service usage

A consumer service registered with an OJS instance can have access to its Journals metadata and files. To do so, it has to
* install this tool (see previous section)
* configure access to OJS instance API
* call an OJS instance API

### Configure access to OJS instance API

### Call an OJS instance API

## License

This program is release under the GNU GPLv3 license. A copy of this license is
available in the file [LICENSE][license].

[license]: ./LICENSE
