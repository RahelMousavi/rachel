
# NTFS Alternate Data Streams (ADS)

## Introduction to NTFS

**NTFS (New Technology File System)** is the default file system used by modern Windows versions.

NTFS supports a feature called **Alternate Data Streams (ADS)**, which allows additional data to be associated with an existing file.

Each NTFS file normally has a primary data stream, also called the default data stream. ADS allows additional named streams to be stored alongside it.

## What Is Alternate Data Stream?

An **Alternate Data Stream (ADS)** is an additional data stream associated with a file on an NTFS volume.

Unlike the default data stream, which contains the regular file content, an alternate stream stores additional information.

ADS can be used for legitimate purposes, including storing metadata and other file-related information.

However, attackers may abuse this feature to hide data or malicious content from ordinary file browsing.

### Important Characteristics of ADS

- An alternate stream is associated with an existing file.
- It can contain data separate from the file's default content.
- It is not normally displayed as a separate file in standard Windows File Explorer views.
- The default file content can remain unchanged when an alternate stream is created.
- Some basic file listing and inspection tools may not display alternate streams.

**Important:** ADS is not inherently malicious. It is a legitimate NTFS feature that can be abused for hiding information.

## How ADS Works

An alternate stream can be referenced using the following syntax:

```text
filename:streamname
```

For example:

```text
report.txt:hidden.txt
```

Here:

- `report.txt` is the existing file.
- `hidden.txt` is the name of the alternate stream.

The alternate stream is associated with `report.txt` rather than appearing as a separate file in a normal directory listing.

### Creating an Alternate Data Stream

The following command demonstrates how to create an alternate stream in Windows:

```cmd
echo This is hidden stream data > report.txt:hidden.txt
```

This command writes data into an alternate stream named `hidden.txt`, associated with `report.txt`.

To read the stream:

```cmd
more < report.txt:hidden.txt
```

To list streams associated with a file, PowerShell can be used:

```powershell
Get-Item .\report.txt -Stream *
```

To read a specific stream:

```powershell
Get-Content .\report.txt -Stream hidden.txt
```

These commands are useful for understanding and inspecting ADS behavior in an authorized Windows lab.

## How Attackers Abuse ADS

Attackers may abuse ADS to hide information or files from ordinary directory listings.

Possible uses include:

- Hiding suspicious data inside an existing file.
- Storing malicious content in an alternate stream.
- Making suspicious data less visible during basic file inspection.
- Attempting to conceal malware-related artifacts.

However, storing executable content in ADS does not automatically make it execute. Additional execution mechanisms would be required.

## Detecting Alternate Data Streams

Because ordinary directory listings may not reveal ADS, specialized inspection methods are useful.

### 1. PowerShell

PowerShell can enumerate alternate streams:

```powershell
Get-Item -Path .\* -Stream *
```

This can help identify streams associated with files in the current directory.

### 2. Streams Utility

Microsoft Sysinternals provides the **Streams** utility for identifying NTFS alternate streams.

It can be used to inspect files and directories for additional data streams.

### 3. ADS Detection Tools

The course lists several tools for identifying alternate streams:

- Stream Armor
- ADS Scanner
- ADS Spy
- List NTFS Streams (LNS)
- Streams
- Stream Detector
- ADS Manager
- NTFS-Stream
- AlternateStreamView
- Stream Explorer
- ADS Detector
- GMER
- HijackThis

These tools are included as course references. Some are legacy tools, so their availability, compatibility, and maintenance status should be checked before use.

## Countermeasures Against ADS Abuse

### 1. Inspect Files for Alternate Streams

Use PowerShell or trusted forensic tools to identify unexpected alternate streams.

### 2. Use File Integrity Monitoring

File integrity monitoring tools can help detect unauthorized changes to files.

For example, **Tripwire** provides file integrity monitoring capabilities.

### 3. Investigate Suspicious Files

Investigate files with unexpected alternate streams, especially in sensitive directories or locations used by applications.

### 4. Restrict File System Permissions

Apply appropriate permissions to prevent unauthorized users from creating or modifying files in sensitive directories.

### 5. Use Security Monitoring Tools

Use endpoint security and monitoring solutions that can inspect suspicious file activity and detect unusual behavior.

### 6. Understand File System Limitations

The course mentions moving suspicious files to a FAT partition as a way to remove NTFS alternate streams.

This can remove ADS because FAT file systems do not support NTFS alternate data streams. However, copying files between file systems should be done carefully because it may change metadata and other file attributes.

For forensic investigations, preserve the original evidence before attempting any modification.

## Summary

NTFS Alternate Data Streams allow additional data to be associated with existing files on an NTFS volume.

Although ADS is a legitimate file system feature, attackers may abuse it to hide data or malicious content.

Important points:

- ADS stores additional data associated with an existing NTFS file.
- Alternate streams are not normally visible in standard directory listings.
- PowerShell and Microsoft Sysinternals Streams can help identify ADS.
- File integrity monitoring and proper access controls help detect and prevent abuse.

Understanding ADS is important for Windows security assessments and digital forensics.

## Related Links

- [Microsoft Learn - File Streams](https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams)
- [Microsoft Sysinternals - Streams](https://learn.microsoft.com/en-us/sysinternals/downloads/streams)
- [Microsoft Learn - Get-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-item)
- [Tripwire](https://www.tripwire.com/)
- [MITRE ATT&CK - Masquerading (T1036)](https://attack.mitre.org/techniques/T1036/)
