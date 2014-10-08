# Original query

```
{
    "location": {
        "ref": "Chr1",
        "start": 658657,
        "objectName": "AT1G02920",
        "tracks": ["SequenceFeature","Gene"],
        "end": 659771
    },
    "name": "glutathione S-transferase 7"
}
```

# Transformed response

The "queryThalemineAsJbrowseIndex" ADAMA service transforms the tracks
array in the resulting JSON objects to use track names that are
congruent with AIP's current Jbrowse instance.

```
{
    "location": {
        "ref": "Chr1",
        "start": 658657,
        "objectName": "AT1G02920",
        "tracks": ["TAIR10_loci"],
        "end": 659771
    },
    "name": "glutathione S-transferase 7"
}
 ```
