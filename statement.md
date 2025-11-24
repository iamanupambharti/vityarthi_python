# Statement of Purpose

## Problem Statement

In many small-scale settings, such as co-working spaces, university computer labs, and local libraries, seat allocation is frequently managed and tracked by hand. This method, which may rely on basic spreadsheets or paper-based systems, is ineffective and prone to human error. Double-booking seats, the inability to promptly ascertain occupancy status, and the absence of historical data are typical problems. A straightforward digital solution is obviously needed to expedite seat distribution, cut down on administrative burden, and guarantee an equitable and well-organized procedure for users.

## Scope of the Project

This project, "Seat Manager", is a command-line interface (CLI) application that is lightweight and intended to make seat management easier. Its focus is on giving a single administrator access to essential features. User creation and management, seat distribution and release, and local data persistence are all made possible by the application. It is intended to be a stand-alone tool without the need for complicated dependencies or a dedicated server. In order to maintain the tool's simplicity and ease of maintenance, features like a graphical user interface, multi-user accounts with varying levels of permission, and network-based access are purposefully left out.


## Target Users

This application's main target users are those in charge of overseeing communal seating areas, such as:

* **Librarians:** To oversee student seating in study areas or computer terminals; * **Lab Administrators:** To supervise student seating in university or school computer labs; * **Co-working Space Managers:** To manage member desk assignments; * **Event Organizers:** For basic seat management at small, one-session events.

The ideal user is someone who requires a simple tool without the complexity of a large-scale enterprise solution to replace a manual or nonexistent system.

## High-Level Features

Using a menu-driven CLI, the application will offer the following essential features:

* **User Creation:** The ability to add new users to the system with a distinct ID, name, and email, such as members or students.
Assign a registered user to a seat that is available. A seat that is already occupied cannot be assigned by the system.
* **Seat Release:** When a user departs, a seat becomes available to others.
* **List and View Status:** Present a thorough list of every seat, indicating which are vacant and which are occupied, along with the occupant's information.
* **Data Persistence:** Ensure that no data is lost between sessions by automatically loading current user and seat data upon startup and offering the option to save all changes upon exit.
* **Logging:** For administrative review, keep a straightforward log of important actions.
