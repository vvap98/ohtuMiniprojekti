"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

FIELDS = {
    "@article": {
        "required": ["author", "title", "journal", "year"],
        "optional": ["volume", "number", "pages", "month", "note"],
    },
    "@book": {
        "required": ["author", "title", "publisher", "year"],
        "optional": [
            "volume", "number", "series", "address", "edition", "month", "note"
        ],
    },
    "@booklet": {
        "required": ["title"],
        "optional": [
            "author", "howpublished", "address", "month", "year", "note"
        ],
    },
    "@inbook": {
        "required": [
            "author", "title", "chapter", "pages", "publisher", "year"
        ],
        "optional": [
            "volume", "number", "series", "type", "address", "edition",
            "month", "note"
        ],
    },
    "@incollection": {
        "required": [
            "author", "title", "booktitle", "publisher", "year"
        ],
        "optional": [
            "editor", "volume", "number", "series", "type", "chapter",
            "pages", "address", "edition", "month", "note"
        ],
    },
    "@inproceedings": {
        "required": ["author", "title", "booktitle", "year"],
        "optional": [
            "editor", "volume", "number", "series", "pages", "address",
            "month", "organization", "publisher", "note"
        ],
    },
    "@conference": {
        "required": ["author", "title", "booktitle", "year"],
        "optional": [
            "editor", "volume", "number", "series", "pages", "address",
            "month", "organization", "publisher", "note"
        ],
    },
    "@manual": {
        "required": ["title"],
        "optional": [
            "author", "organization", "address", "edition", "month",
            "year", "note"
        ],
    },
    "@mastersthesis": {
        "required": ["author", "title", "school", "year"],
        "optional": ["type", "address", "month", "note"],
    },
    "@phdthesis": {
        "required": ["author", "title", "school", "year"],
        "optional": ["type", "address", "month", "note"],
    },
    "@proceedings": {
        "required": ["title", "year"],
        "optional": [
            "editor", "volume", "number", "series", "address", "month",
            "organization", "publisher", "note"
        ],
    },
    "@techreport": {
        "required": ["author", "title", "institution", "year"],
        "optional": ["type", "number", "address", "month", "note"],
    },
    "@unpublished": {
        "required": ["author", "title", "note"],
        "optional": ["month", "year"],
    },
    "@misc": {
        "required": [],
        "optional": [
            "author", "title", "howpublished", "month", "year", "note"
        ],
    },
}

def create_required_input(field: str) -> rx.Component:
    """create input field"""
    return rx.input(
        name=field,
        placeholder=field,
        required=True,
    )

def create_optional_input(field: str) -> rx.Component:
    """create input field"""
    return rx.input(
        name=field,
        placeholder=field,
    )

class State(rx.State):
    """The app state."""
    selected_type = "@article"

    @rx.event
    def set_selected(self, value: str):
        """Set selected reference type"""
        self.selected_type = value

    @rx.var
    def required_inputs(self) -> list[str]:
        """Return required fields for current reference type"""
        return FIELDS[self.selected_type]["required"]

    @rx.var
    def optional_inputs(self) -> list[str]:
        """Return optional fields for current reference type"""
        return FIELDS[self.selected_type]["optional"]

    @rx.event
    def submit(self, form_data):
        """Print form"""
        print(form_data)

def index() -> rx.Component:
    """Form"""
    return rx.container(
        rx.form(
            rx.vstack(
                rx.select(
                    FIELDS,
                    value = State.selected_type,
                    on_change = State.set_selected,
                    name="type_selector",
                ),

                rx.text("Required fields"),
                rx.foreach(
                    State.required_inputs,
                    create_required_input,
                ),

                rx.text("Optional fields"),
                rx.foreach(
                    State.optional_inputs,
                    create_optional_input,
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=State.submit,
        )
    )


app = rx.App()
app.add_page(index)
