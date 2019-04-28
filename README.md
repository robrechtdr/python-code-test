# Ostmodern Python Code Test

The goal of this exercise is to test that you know your way around Django and
REST APIs. Approach it the way you would an actual long-term project.

The idea is to build a platform on which your users can buy and sell Starships.
To make this process more transparent, it has been decided to source some
technical information about the Starships on sale from the [Starship
API](https://swapi.co/documentation#starships).

A Django project some initial data models have been created already. You may need
to do some additional data modelling to satify the requirements.

## Getting started

* This test works with either
  [Docker](https://docs.docker.com/compose/install/#install-compose) or
  [Vagrant](https://www.vagrantup.com/downloads.html)
* Get the code from `https://github.com/ostmodern/python-code-test`
* Do all your work in your own `develop` branch
* Once you have downloaded the code the following commands will get the site up
  and running

```shell
# For Docker
docker-compose up
# You can run `manage.py` commands using the `./manapy` wrapper

# For Vagrant
vagrant up
vagrant ssh
# Inside the box
./manage.py runserver 0.0.0.0:8008
```
* The default Django "It worked!" page should now be available at
  http://localhost:8008/

## Tasks

Your task is to build a JSON-based REST API for your frontend developers to
consume. You have built a list of user stories with your colleagues, but you get
to decide how to design the API. Remember that the frontend developers will need
some documentation of your API to understand how to use it.

We do not need you to implement users or authentication, to reduce the amount of
time this exercise will take to complete. You may use any external libraries you
require.

1. We need to be able to import all existing
  [Starships](https://swapi.co/documentation#starships) to the provided Starship
  Model
2. A potential buyer can browse all Starships
3. A potential buyer can browse all the listings for a given `starship_class`
4. A potential buyer can sort listings by price or time of listing
5. To list a Starship as for sale, the user should supply the Starship name and
  list price
6. A seller can deactivate and reactivate their listing

After you are done, create a release branch in your repo and send us the link.

## Solution

1. See [import_starships management command](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/management/commands/import_starships.py).

    You can check this yourself by running `./manapy import_starships`

    ![import_starships](https://raw.githubusercontent.com/robrechtdr/python-code-test/develop/.misc/import_starships.png)

    then check `http://0.0.0.0:8080/starships/` and you will see:

    ![starships_browsable](https://raw.githubusercontent.com/robrechtdr/python-code-test/develop/.misc/starhips_browsable.png)

2. See [test_browse_starships test](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/tests.py#L23).

    Run these tests via `./manapy test -v2 shiptrader` 

    ![starship_tests](https://raw.githubusercontent.com/robrechtdr/python-code-test/develop/.misc/starship_tests.png)


3. See [test_get_specific_starship_class_listings](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/tests.py#L33).
4.
    1. See [test_get_price_sorted_listings](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/tests.py#L43).
    2. See [test_get_time_sorted_listings](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/tests.py#L52).
5. See [test_list_starship_for_sale](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/tests.py#L68).
6. See [test_deactivate_listing](https://github.com/robrechtdr/python-code-test/blob/develop/testsite/shiptrader/tests.py#L84).

You can also set up some dummy listings conveniently via `./manapy dummy_populate`,
then run `docker-compose up` and visit `http://0.0.0.0:8080/listings/`:

![listings_browsable](https://raw.githubusercontent.com/robrechtdr/python-code-test/develop/.misc/listings_browsable.png)


### Notes

* Upgraded project to work with latest LTS Django version (2.2). 
* Did not use swapi's Python SDK as it is Python2.7.x and this project is using Python3.6.
* Wiped previous migration file as project still brand new and assume never populated with relevant data.
* Some 'niceties' like a view-specific custom search param is not supported yet officially in DRF 2.2 at the time. A solution via a drf-suggested third party lib would require diving deeper into the rabbithole.
* No considerations around other environments like prod or staging were made. 
* Endpoints were not fine-tuned to restrict functionality to merely what was asked. As implemented you can e.g. also make a listing or starship detail call. 
* With DRF would be simple to add pagination if requested.
* A next level would be implementing users who can buy and sell. You would also want authentication and restrict user api access appropriately like allowing a user to only deactivate their own listing entries. 
* If the swapi starship list would have been something that grew over time, it would be nice to run the import via a cron task and as a batch process (as multiple pages) via Celery.
* See commit messages for more details about rationale behind changes.
