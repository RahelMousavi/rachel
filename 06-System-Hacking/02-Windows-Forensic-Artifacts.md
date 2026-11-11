
# Windows Forensic Artifacts

## Introduction to Windows Forensic Artifacts

Windows stores different types of information about system activity, file usage, application execution, and system state.

These records and artifacts can help investigators understand what happened on a computer.

During an attack, an attacker may attempt to disable certain features or remove artifacts to make forensic investigation more difficult.

This section covers several Windows features that can preserve useful forensic information.

## 1. Last Access Timestamp

The **Last Access Timestamp** is a file-system timestamp that records information about when a file or directory was last accessed.

Depending on the file system and Windows configuration, this timestamp may be updated when a file is read or opened.

### Why Is It Important?

Last Access timestamps can provide useful information during forensic investigations.

For example, they may help investigators determine whether a particular file was accessed during a suspicious period.

However, Last Access updates may be disabled, delayed, or affected by system configuration.

### Disabling Last Access Updates

Windows provides the `fsutil` utility to inspect and configure certain file-system behaviors.

The course introduces the following command as an example of disabling Last Access timestamp updates:

```cmd
fsutil behavior set disablelastaccess 1
```

From a defensive perspective, unexpected changes to this setting may reduce the availability of useful file-access metadata.

The setting can be inspected with:

```cmd
fsutil behavior query disablelastaccess
```

**Important:** Last Access timestamps are only one source of evidence. Their absence does not prove that a file was never accessed.

## 2. Windows Hibernation

**Hibernation** is a Windows power-management feature that saves the current system state to disk so that the computer can resume later.

When Windows enters hibernation, it stores relevant memory contents in a system file named:

`hiberfil.sys`

This file is normally located in the root directory of the system drive.

### Why Is Hibernation Important in Forensics?

The hibernation file may contain information from system memory at the time hibernation occurred.

Depending on the system state and configuration, this information may help investigators examine:

- Running processes.
- Open applications.
- Data that was present in memory.
- Other system-state information.

Forensic tools may analyze this file to recover useful evidence.

### Disabling Hibernation

The course explains that disabling hibernation prevents Windows from creating or maintaining the hibernation file in the usual way.

An attacker may attempt this to reduce the availability of memory-related forensic evidence.

For defenders, unexpected changes to hibernation settings should be investigated, especially on systems where memory artifacts are important.

## 3. Windows Virtual Memory - Paging File

**Virtual Memory** is a memory-management feature that allows Windows to use disk storage as an extension of physical RAM.

The file used for this purpose is commonly called the **Paging File**:

`pagefile.sys`

When physical memory is insufficient or when memory-management policies require it, Windows may move memory pages to disk.

### Why Is the Paging File Important in Forensics?

The paging file may contain fragments of information that were previously present in memory.

Depending on system activity, it may contain:

- Application data.
- Fragments of documents.
- Parts of sensitive information.
- Other memory-related artifacts.

This can make the paging file useful during forensic analysis.

### Disabling the Paging File

The course discusses disabling virtual memory as a way an attacker might attempt to reduce the amount of information written to disk.

However, disabling the paging file is not a reliable way to remove existing evidence. It can also affect system stability and performance.

For defenders, preserving the paging file may be important when investigating a compromised system.

## 4. System Restore Points

**System Restore** is a Windows feature that allows users to return certain system settings and components to an earlier state.

Windows creates restore points that may contain information about system configuration and selected files.

### Why Are Restore Points Important in Forensics?

Restore points may help investigators identify:

- Previous system configurations.
- Changes to system files.
- Evidence of earlier software installations.
- Information about files or system states that have changed.

Restore points are not complete backups of all user data, and they do not preserve every deleted file.

### Disabling System Restore

An attacker may attempt to disable System Protection or remove restore points to reduce the availability of historical system information.

Unexpected changes to System Restore settings should be treated as potentially suspicious.

For defenders, restore points and other recovery data should be protected according to the organization's retention and recovery policies.

## 5. Windows Thumbnail Cache

Windows creates thumbnail previews for certain image and document files to make browsing folders faster.

A thumbnail cache may contain small preview images of files that were previously viewed.

Depending on the Windows version and configuration, thumbnail data may be stored in database files such as:

`thumbs.db`

### Why Is Thumbnail Cache Important in Forensics?

Thumbnail caches may preserve previews of files even after the original files have been moved or deleted.

For example, a thumbnail may provide evidence that an image or document previously existed on the system.

This information can help investigators understand previous user activity.

### Disabling Thumbnail Caching

The course discusses disabling thumbnail caching as a way to reduce the creation of these artifacts.

From a defensive perspective, unexpected changes to thumbnail-cache settings may be relevant during an investigation.

**Important:** The location and behavior of thumbnail caches vary across Windows versions. `thumbs.db` is not the only location where thumbnail data may be stored.

## 6. Windows Prefetch

**Prefetch** is a Windows performance feature designed to help applications and system components load more efficiently.

Windows may create Prefetch files containing information related to application execution.

These files are commonly stored in:

`C:\Windows\Prefetch\`

### Why Is Prefetch Important in Forensics?

Prefetch artifacts can provide useful information about program execution.

Depending on the Windows version and available data, investigators may use them to examine:

- Whether an application was executed.
- Approximate execution times.
- Application-related file activity.
- Other execution-related details.

Prefetch information can help reconstruct activity on a system.

### Disabling Prefetch

An attacker may attempt to disable Prefetch to reduce the creation of execution-related artifacts.

However, Prefetch is a performance feature, and its behavior varies depending on the Windows version and system configuration.

Unexpected changes to Prefetch settings should be investigated rather than automatically treated as proof of malicious activity.

## Summary

Windows creates several artifacts that can help investigators reconstruct system activity.

Important examples include:

- **Last Access Timestamp:** Provides information about file-access activity.
- **Hibernation File (`hiberfil.sys`):** May preserve memory-related information when the system hibernates.
- **Paging File (`pagefile.sys`):** May contain fragments of data previously stored in RAM.
- **System Restore Points:** Preserve selected historical system information.
- **Thumbnail Cache:** May contain previews of files previously viewed.
- **Prefetch:** Provides information related to application execution.

Attackers may attempt to disable or remove these artifacts to make forensic investigations more difficult.

Security professionals should understand how these artifacts are created, preserve them during investigations, and monitor unexpected changes to related system settings.

## Related Links

- [Microsoft Learn - Fsutil Behavior](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-behavior)
- [Microsoft Learn - Hibernation](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options)
- [Microsoft Learn - Virtual Memory](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/introduction-to-the-page-file)
- [Microsoft Learn - System Protection](https://support.microsoft.com/en-us/windows/system-protection)
- [Microsoft Learn - Windows File Systems](https://learn.microsoft.com/en-us/windows/win32/fileio/file-systems)
- [MITRE ATT&CK - Indicator Removal](https://attack.mitre.org/tactics/TA0005/)
