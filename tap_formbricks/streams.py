"""Stream type classes for tap-formbricks."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_formbricks.client import FormbricksStream

class PersonsStream(FormbricksStream):
    """Define people stream."""

    name = "people"
    path = "/management/people"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The unique identifier for the record."),
        th.Property("userId", th.StringType, description="The unique identifier for the person."),
        th.Property(
            "attributes",
            th.ObjectType(
                additional_properties=True,
            ),
            description="A set of custom attributes associated with the person."
        ),
        th.Property("createdAt", th.DateTimeType, description="Timestamp of when the person was created."),
        th.Property("updatedAt", th.DateTimeType, description="Timestamp of when the person was last updated."),
        th.Property("environmentId", th.StringType, description="The identifier for the environment.")
    ).to_dict()

class SurveysStream(FormbricksStream):
    """Define surveys stream."""

    name = "surveys"
    path = "/management/surveys"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The unique identifier for the survey."),
        th.Property("createdAt", th.DateTimeType, description="The timestamp when the survey was created."),
        th.Property("updatedAt", th.DateTimeType, description="The timestamp when the survey was last updated."),
        th.Property("name", th.StringType, description="The name of the survey."),
        th.Property("type", th.StringType, description="The type of the survey."),
        th.Property("environmentId", th.StringType, description="The identifier for the environment in which the survey was created."),
        th.Property("createdBy", th.StringType, description="The identifier of the user who created the survey."),
        th.Property("status", th.StringType, description="The status of the survey (e.g., inProgress, completed)."),
        th.Property(
            "welcomeCard",
            th.ObjectType(
                th.Property("html", th.ObjectType(th.Property("default", th.StringType, description="HTML content of the welcome card."))),
                th.Property("enabled", th.BooleanType, description="Whether the welcome card is enabled."),
                th.Property("fileUrl", th.StringType, description="The URL of the welcome card file."),
                th.Property("headline", th.ObjectType(th.Property("default", th.StringType, description="The headline of the welcome card."))),
                th.Property("timeToFinish", th.BooleanType, description="Whether to show the time to finish."),
                th.Property("showResponseCount", th.BooleanType, description="Whether to show the response count on the welcome card.")
            ),
            description="Details of the welcome card displayed at the beginning of the survey."
        ),
        th.Property(
            "questions",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType, description="The unique identifier for the question."),
                    th.Property("type", th.StringType, description="The type of question (e.g., openText, multipleChoiceMulti)."),
                    th.Property("headline", th.ObjectType(th.Property("default", th.StringType, description="The headline of the question."))),
                    th.Property("required", th.BooleanType, description="Whether the question is mandatory."),
                    th.Property(
                        "choices",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.StringType, description="The unique identifier for the choice."),
                                th.Property("label", th.ObjectType(th.Property("default", th.StringType, description="The label text for the choice.")))
                            )
                        ),
                        description="List of choices for multiple choice questions."
                    )
                )
            ),
            description="The list of questions included in the survey."
        ),
        th.Property(
            "endings",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType, description="The unique identifier for the ending screen."),
                    th.Property("type", th.StringType, description="The type of ending screen."),
                    th.Property("headline", th.ObjectType(th.Property("default", th.StringType, description="The headline for the ending screen."))),
                    th.Property("subheader", th.ObjectType(th.Property("default", th.StringType, description="The subheader for the ending screen."))),
                    th.Property("buttonLink", th.StringType, description="The link for the button on the ending screen."),
                    th.Property("buttonLabel", th.ObjectType(th.Property("default", th.StringType, description="The label for the button on the ending screen.")))
                )
            ),
            description="The ending screens for the survey."
        ),
        th.Property(
            "hiddenFields",
            th.ObjectType(
                th.Property("enabled", th.BooleanType, description="Whether hidden fields are enabled."),
                th.Property("fieldIds", th.ArrayType(th.StringType), description="List of field IDs that are hidden.")
            ),
            description="Hidden fields associated with the survey."
        ),
        th.Property("displayOption", th.StringType, description="Display option for the survey (e.g., displayOnce)."),
        th.Property("recontactDays", th.IntegerType, description="Number of days before recontacting the user."),
        th.Property("displayLimit", th.IntegerType, description="The display limit for the survey."),
        th.Property("autoClose", th.BooleanType, description="Whether the survey auto-closes after a period."),
        th.Property("runOnDate", th.DateTimeType, description="The date the survey should start running."),
        th.Property("closeOnDate", th.DateTimeType, description="The date the survey should stop running."),
        th.Property("delay", th.IntegerType, description="The delay time before displaying the survey."),
        th.Property("displayPercentage", th.IntegerType, description="The percentage of users to display the survey to."),
        th.Property("autoComplete", th.BooleanType, description="Whether the survey automatically completes."),
        th.Property("isVerifyEmailEnabled", th.BooleanType, description="Whether email verification is enabled."),
        th.Property("redirectUrl", th.StringType, description="The URL to redirect users to after completing the survey."),
        th.Property("surveyClosedMessage", th.StringType, description="Message to show when the survey is closed."),
        th.Property(
            "singleUse",
            th.ObjectType(
                th.Property("enabled", th.BooleanType, description="Whether the survey can be used only once."),
                th.Property("isEncrypted", th.BooleanType, description="Whether single-use responses are encrypted.")
            ),
            description="Settings for single-use surveys."
        ),
        th.Property("pin", th.StringType, description="The pin for the survey.")
    ).to_dict()

class ResponsesStream(FormbricksStream):
    """Define responses stream."""

    name = "responses"
    path = "/management/responses"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The unique identifier for the response."),
        th.Property("createdAt", th.DateTimeType, description="The timestamp when the response was created."),
        th.Property("updatedAt", th.DateTimeType, description="The timestamp when the response was last updated."),
        th.Property("surveyId", th.StringType, description="The identifier for the related survey."),
        th.Property("finished", th.BooleanType, description="Whether the response was completed."),
        th.Property(
            "data",
            th.ObjectType(
                additional_properties=True,
            ),
            description="Survey question responses."
        ),
        th.Property(
            "meta",
            th.ObjectType(
                additional_properties=True,
            ),
            description="Metadata about the response."
        ),
        th.Property("language", th.StringType, description="Language code of the response, if provided."),
        th.Property(
            "person",
            th.ObjectType(
                th.Property("id", th.StringType, description="The unique identifier for the person.")
            ),
            description="Information about the person who submitted the response."
        ),
        th.Property("tags", th.ArrayType(th.StringType), description="Tags associated with the response."),
        th.Property("notes", th.ArrayType(th.StringType), description="Notes related to the response.")
    ).to_dict()

class ActionClassesStream(FormbricksStream):
    """Define action classes stream."""

    name = "action-classes"
    path = "/management/action-classes"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The unique identifier for the action class."),
        th.Property("createdAt", th.DateTimeType, description="The timestamp when the action class was created."),
        th.Property("updatedAt", th.DateTimeType, description="The timestamp when the action class was last updated."),
        th.Property("name", th.StringType, description="The name of the action class."),
        th.Property("description", th.StringType, description="Description of the action class."),
        th.Property("type", th.StringType, description="Type of the session event (e.g. automatic)."),
        th.Property("environmentId", th.StringType, description="The identifier for the environment.")
    ).to_dict()

class AttributeClassesStream(FormbricksStream):
    """Define attribute classes stream."""

    name = "attribute-classes"
    path = "/management/attribute-classes"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The unique identifier for the attribute class."),
        th.Property("createdAt", th.DateTimeType, description="The timestamp when the attribute class was created."),
        th.Property("updatedAt", th.DateTimeType, description="The timestamp when the attribute class was last updated."),
        th.Property("name", th.StringType, description="The name of the attribute class."),
        th.Property("description", th.StringType, description="Description of the attribute class."),
        th.Property("archived", th.BooleanType, description="Whether the attribute class is archived."),
        th.Property("type", th.StringType, description="Type of the attribute class (e.g. text)."),
        th.Property("environmentId", th.StringType, description="The identifier for the environment.")
    ).to_dict()