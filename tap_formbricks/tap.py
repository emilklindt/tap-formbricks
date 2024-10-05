"""Formbricks tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_formbricks import streams

class TapFormbricks(Tap):
    """Formbricks tap class."""

    name = "tap-formbricks"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="The key to authenticate against the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.FormbricksStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.PersonsStream(self),
            streams.SurveysStream(self),
            streams.ResponsesStream(self),
            streams.ActionClassesStream(self),
            streams.AttributeClassesStream(self),
        ]


if __name__ == "__main__":
    TapFormbricks.cli()
