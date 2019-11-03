# HackOHI.O

Data For OSU Hackathon

There are two types of files, data and config, linked on the column MeterID.

## Data Files

The data files contain time series data for the challenge. Each meter represents
the consumption for one of the following resources: Chilled Water, Heating Hot
Water, Steam, or Electricity. Each meter has two years (or less in some cases)
of usage. There are three files. One contains daily data for all meters. Two
others are hourly data split into two files due to size limitations.

| Field Name   | Field Description                                                                    |
| ------------ | ------------------------------------------------------------------------------------ |
| MeterID      | Meter identifier, will have a match in the config file                               |
| CurrentValue | Most precise measurement value                                                       |
| ValueString  | Less precise measurement value                                                       |
| Time         | Time of measurement in UTC, format yyyy-mm-ddThh:mm:ssZ                              |
| Status       | Sometimes meters malfunction, this indicates if this measurement is OK or UNRELIABLE |
| StatusCode   | Numeric representation of status                                                     |

## Config Files

The config file contains metadata for the challenge. Each meter represents
consumption for a building. Meter and building attributes are included here, if
available.

| Field Name           | Field Description                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| BuildingID           | ID for the building where this meter is located                                                 |
| MeterID              | Meter identifier, will have a match in the config file                                          |
| Description          | Description of what the meter is measuring                                                      |
| Units                | Unit of measurement for this meter                                                              |
| Resource             | Resource measured by this meter, can be Chilled Water, Heating Hot Water, Steam, or Electricity |
| BuildingName         | Name of this building                                                                           |
| GrossSquareFeet      | Size of this building in square feet                                                            |
| BuildDate            | Construction date of this building                                                              |
| Latitude             | Latitude coordinate of this building                                                            |
| Longitude            | Longitude coordinate of this building                                                           |
| Campus               | Can be Main or Medical Center                                                                   |
| Organization         | Organization which manages this building                                                        |
| LocationType         | Category of usage of this building                                                              |
| SteamSourceID        | BuildingID representing the source of steam of this building (1)                                |
| ChilledWaterSourceID | BuildingID representing the source of chilled water of this building (1)                        |
| HotWaterSourceID     | BuildingID representing the source of hot water of this building (1)                            |
| ActivationDate       | The date/tiem this meter started reporting data                                                 |

1. Some buildings are supplied by other buildings on campus and will have
   values, others are supplied by external sources and will not have values.
