# omni_filecheck

## Goal

File verification of Adobe Omniture files before processing.
Omniture suite file exports usually deliver an additional file
containing metadata like this

```
Datafeed-Manifest-Version: 1.0
Lookup-Files: 1
Data-Files: 1
Total-Records: 114470

Lookup-File: omni_20160622-000000-lookup_data.tar.gz
MD5-Digest: 1b8307f057dbd01be01117f39ffead77
File-Size: 478

Data-File: 01-omni_20160622-000000.tsv.gz
MD5-Digest: dbfab5f507fb297f408c8738a84348b8
File-Size: 6913007
Record-Count: 114470
```

This project tries to parse this metadata and verify against the
delivered lookup and data files.

By now these checks are implemented:

- file presence
- checksum (md5)
- file size

## TODO

- Verify record count (full and by file)
- Correct parsing of lookup- and data files
- Logging
- Testing
