# Introduction to Clearing Directory

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/CA/Clearing_Directory_(CA)/Misc/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm) > Introduction

- [Clearing Directory Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm)
  - [Introduction](../../Clearing_Directory_(CA)/Misc/Introduction.htm)
  - [Configuration](../../Clearing_Directory_(CA)/Misc/Configuration.htm)
  - [Working with](../../Clearing_Directory_(CA)/Misc/Working_with.htm)
  - [Tasks](../../Clearing_Directory_(CA)/Misc/Tasks.htm)
  - [Outputs](../../Clearing_Directory_(CA)/Misc/Outputs.htm)

Payments

# Introduction to Clearing Directory

Updated On 10 July 2024 |
 15 Min(s) read

Feedback
Summarize

This section gives an introduction to Clearing Directory.

## Clearing Directory Upload

The bank needs to be registered with a clearing to participate in the services it provides. Each clearing releases a clearing directory file or participant bank catalogue that lists the banks participating with the clearing.

The user can identify the participant bank using a Bank Identifier Code (BIC) or National Clearing Code (NCC). Temenos Payment Hub (TPH) can receive the clearing directory file and upload the information to the TPH clearing directory table through an automated process. The received file can be:

- Full file − Lists all the participant banks in the clearing
- Delta file − Contains only the changes from the previous clearing directory release

Each clearing directory file has a different upload API, which maps the information from the directory file to the TPH clearing directory table.

- Existing records that are used for ongoing payment processing co-exist with the newly uploaded records until the purge process happens

If the effective date provided in the file is same or before the date of upload, the API that is uploaded updates the effective date of the records to the next calendar date. This API determines the reachability key based on the configured parameters and stores it in the clearing directory record. This key is used to perform reachability check.

An obsolete record can be deleted from TPH (if configured). The bank user has the flexibility to add new records and view, edit or delete the existing records in the clearing directory table.

If automatic upload of the directory file fails, TPH mark the operation as ‘failed’ and the file is made available in the folder from which it is uploaded. The following clearing directories are loaded to TPH:

| Clearing Directory Upload | File Format | Time Span for Publish | Details Loaded to the System |
| --- | --- | --- | --- |
| HCTINST | GIRO receives the record in GVT file | Monthly | - Bank Identifier Code (BIC) - National Clearing Code (NCC) - Name of the participant bank - Reachability type - Intermediary institution BIC - Status - AFR type - AFR type code - Effective date - Start date - End date |
| EQUENS | Receives record in the EQUENS Reach Table published by the equensWorldline in rocs format | Weekly | - BIC - Payment channel - Name of the participant - Country - Scheme - Reachability type - Status - Start date - End date - Effective date   Other clearing specific details are loaded to clearing specific context name and value pair fields. |
| SIC | Receives record in the SIC Bank Clearing Master Data file published by the SIX Interbank Clearing | Weekly | - BIC - SIC number - Payment channel - Name of participant - City - Country - Scheme - Reachability type - Status - Start date - End date - Effective date   Other clearing specific details are loaded to clearing specific context name or value pair field. |
| STEP2 |  |  | - BIC - Channel - Name of participant - Scheme - Reachability type - Settlement BIC - Status - Start date - Intermediary institution BIC (if available) - End date - Effective date - Admission profile - AOS |
| EBAINST |  |  | - BIC - Channel - Name of participant - Scheme - Reachability type - Settlement BIC - Status - Start date - Intermediary institution BIC (if available) - End date - Effective date - Admission profile - AOS |
| TIPSRTF (EBA RT1) | Receives TIPS RTF published by RT1 clearing |  | - BIC - Channel - Name of participant - Scheme - Reachability type - Settlement BIC - Status - Start date - Intermediary institution BIC (if available) - End date - Effective date - AOS |
| TARGET2 |  |  | - BIC - Payment channel - NCC - Modification flag - Name of institution - City - Scheme - Reachability type - Intermediary institution BIC (if available) - Settlement BIC - Start date - End date - Effective date - Payment date is less than the end date |
| EISCD | Local clearing details of UK (FPS, CHAPS, CNCC, BACS) are loaded to the system from the EISCD Clearing Directory file, which is distributed by Vocalink Limited | Weekly or Monthly | - BIC - Payment channel - NCC - Name of participant - City - Country - Scheme - Reachability type - Intermediary institution BIC (only applicable for CHAPS) - Intermediary NCC (applicable for BACS and CNCC) - Status - Start date - End date - Effective date   Other clearing-specific details are loaded to clearing specific context name or value pair field. |
| HKFPS | HKFPS Participant Subscription CSV Data File is distributed by HKFPS to all payment participants of HKFPS as a ‘full file’ |  | - NCC - Payment channel - Scheme - Institution name - Reachability type - Currency - Status - Effective date - Start date - End date   Other clearing specific details are loaded to clearing-specific context name and value pair fields. |
| HKCHATS | Receives records from HKICL in .txt format | Daily | - BIC - NCC - Institution Name - Scheme - Reachability Type - Currency   Other clearing specific details are loaded to clearing specific context name and value pair fields. |
| BECS Direct Entry | BSB upload file is distributed to all payment participants of BECS every month as a ‘full file’ or ‘delta file’ in CSV format. |  | - NCC - BIC - Modification flag - Payment channel - Institution name - City - Status - Effective date - Start date - Reachability type   Other clearing-specific details are loaded to clearing-specific context name and value pair fields. |
| SYGMA | The clearing directory file of SYGMA is circulated by the BEAC as a full file in XML format. |  | - BIC - Scheme - Payment Channel - Start date - End date - Effective date - Country - Institution Name   Other clearing-specific details are loaded to clearing-specific context name and value pair fields. |
| SYSTAC | The clearing directory file of SYSTAC is circulated by the BEAC 'txt' format. |  | - NCC - Institution Name - Country - Payment Channel - Scheme - City - Start Date - End Date - Effective Date   Other clearing-specific details are loaded to clearing-specific context name and value pair fields. |
| VIBER | Receives the record in the GVT file published by the GIRO | Monthly | - BIC - Payment channel - NCC - Institution name - Scheme - Reachability type - Intermediary institution BIC - Status - Start date - End date - Effective date - VIBER reachability |
| IG2 | Receives record in the GVT file published by the GIRO | Monthly | - BIC - Payment channel - NCC - Institution name - Scheme - Reachability type - Intermediary institution BIC - Status - Start date - End date - Effective date |
| RPS SEPA Clearer (RPSSCL) | German Bundesbank publishes the records | Weekly | - BIC - Payment channel - Name of the participant - Modification flag - Country - Scheme - Reachability type - Intermediary institution (if available) - Start date - End date - Effective date - Status   Other clearing-specific details are loaded to clearing-specific context name or value pair field. |
| SIBTEL | The clearing directory file of SIBTEL is circulated by SIBTEL in ‘.txt’ format |  | - NCC - Institution name - Payment channel - Start date - End date - Effective date |
| SLIPS | The clearing directory file of SLIPS is circulated by Lanka Clearing in ‘.csv’ format | Irregular intervals | - Payment channel - NCC - Institution name - Start date - End date - Effective date - Status   Other clearing-specific details are loaded to clearing-specific context name or value pair field. |
| TIPS | The clearing directory file of TARGET Instant Payment Settlement (TIPS) is circulated by CRDM of TARGET services in ‘.xml’ format  The name of the flat file that contains the TIPS directory should be in the following format:  TIPSDIRTTTTYYYYMMDD, where   - TTTT is the type. For example, FULL for the full version and DLTA for the delta version. - YYYYMMDD specifies the year, month, and date as of which the TIPS directory is valid. | Daily | - Modification flag - Payment channel - BIC - Institution name - Scheme - Reachability type - Intermediary institution BIC - Settlement BIC - Status - Start date - End date - Upload date - Effective date - Upload file name - Maximum Amount |

## Reachability Check

TPH performs reachability check only for outgoing payments. The system performs a validation to check if the beneficiary bank can participate in a specific clearing directly or through an indirect participant.

The reachability API refers to the records stored in the clearing directory table using the reachability key (user configured) to perform reachability check. If a valid record for the BIC or NCC is not found, TPH routes the payment to the Repair queue for user action.

Reachability check is performed in TPH (for every clearing) or Payment Order (for each product), if configured. A participant bank is considered reachable only when a valid record exists in the directory for the specific BIC or NCC for the defined set of parameters.

| Reachability | Condition |
| --- | --- |
| HCTINST | - National Clearing Code (NCC) - Channel = HCTINST - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date - Status = ENABLED |
| EQUENS | - Bank Identifier Code (BIC) - Scheme = CT-INST, CT- INSTTC01 or CT- INSTNT01 - Channel = EWINST - Status = ENABLED - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date |
| SIC | - BIC or NCC (SIC number) − If both BIC and NCC is available, BIC is used to perform reachability check - Branch ID of bank (used together with BIC or SIC number) - Scheme = CT - Payment Channel = SIC - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date - Status = ENABLED |
| STEP2 | - BIC - Payment Channel = STEP2 - SCHEME= SCT, SDDB2B or SDDCORE - Status = ENABLED or R-Only - Payment date is greater than the start and effective date - Payment date is less than the end date |
| EBAINST | - BIC - Payment Channel = EBAINST - SCHEME= SCI - Status = ENABLED or R-Only - Payment date is greater than the start and effective date - Payment date is less than the end date - AOS List not equal to TEC (only for Credit transfer payments) |
| TARGET2 | - BIC - Scheme = CT - Payment Channel = TARGET2 - Payment date is greater than the start and effective date - Status = ENABLED |
| TIPS | - BIC - Scheme = CT - Payment Channel = TIPS - Payment date is greater than the start and effective date - Payment amount is less than or equal to EUR 100,000.00 - Status = ENABLED |
| CHAPS | - BIC or NCC - Scheme = \*, DD or CT - Payment Channel = STG - End date of the record is either blank or greater than the payment execution date - Bank Office Indicator = M or L - Status is not equal to N |
| CNCC | - BIC or NCC - Scheme = \*, CT or DD - Payment Channel = CNCC - End date of the record is either blank or greater than the payment execution date - Bank Office Indicator = M or L - Status is not equal to N |
| FPS | - BIC or NCC - Scheme = \*, CT or DD - Payment Channel = FPS - End date of the record is either blank or greater than the payment execution date - Bank Office Indicator = M or L - Status is not equal to N |
| BACS | - BIC or NCC - Scheme = \*, CT or DD - Payment Channel = BACS - End date of the record is either blank or greater than the payment execution date - Bank Office Indicator = M or L - Status is not equal to N - Transaction Type = 01, 07, 17, 18, 19, 99, 13, Z4, Z5 or blank - Does not have disallowed entry |
| UK BACS AUDDIS Check (If BACS and *Electronic Mandate Check* is set to Y) | - BIC or NCC - Channel = BACS - Status not equal to N - Bank Office Type Indicator = M or L - Scheme = CT or DD - Transaction Type = 01, 07, 17, 18, 19, 99, 13, Z4, Z5 or blank - Allows Direct Debit (DR) service - *DDI Voucher Flag* is not equal to Y |
| HKFPS | - NCC - Scheme = CT-PAYC01 or CT-PAYC02 - Payment Channel = HKFPSINST - Payment Currency - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date - Status = ENABLED |
| HKCHATS | - BIC/NCC - Channel = CHATSMX - Scheme = \*-(Ccy) - Payment date is greater than the start and effective date - Status = ENABLED |
| BECS Direct Entry | - NCC - Payment Channel = BECS - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date - Status = ENABLED |
| SYGMA | - BIC - Payment Channel = SYGMA - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date - Status = ENABLED |
| SYSTAC | - Bank Code (National Clearing Code) - Payment Channel = SYSTAC - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date - Status = ENABLED |
| VIBER | Reachability check is performed for both sending bank and receiving bank.  **Sending Bank**   - NCC - Payment channel = HUF - Status = ENABLED - VIBER reachability = S or B - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date   **Receiving Bank**   - NCC - Payment channel = HUF - Status = ENABLED - VIBER reachability = R or B - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date |
| IG2 | - NCC - Payment channel = IG2 - Status = ENABLED - Payment date is greater than or equal to the start and effective date - Payment date is less than or equal to the end date |
| RPSSCL | - BIC - Scheme = SCT, SDDcore, SDDcoreR-Txonly or SDDb2bR-Txonly - Payment Channel = RPSSCL - Status = ENABLED - Payment date (current date) is greater than or equal to the start and effective date - Payment date (current date) is lesser than or equal to the end date (if available) |

## License Codes

TPH performs clearing directory upload and reachability check for the following clearings:

| Clearing | License Code |
| --- | --- |
| EISCD UK Clearing Directory (BACS, FPS,CHAPS, CNCC) | CAIEIS |
| HCTINST Directory Upload (Feature) | CAIHCT |
| EQUENS Instant Directory Upload (Feature) | CAINCT |
| SIC Directory Upload (Feature) | CAISIC |
| HKFPS Directory Upload | CAHINS |
| HKCHATS Directory Upload | CAHKRX |
| BECS Direct Entry Directory Upload | CAAUST |
| SYGMA Clearing Directory | CASYGM |
| SYSTAC Clearing Directory | CASYTC |
| VIBER Directory Upload | CAIHCT |
| IG2 Directory Upload | CAIHCT |
| RPSSCL | CARPSS |
| SIBTEL | CATNCL |
| SLIPS Directory Upload | CALKCL |
| TIPS Directory Upload | CAITIP |

In this topic

- [Introduction to Clearing Directory](#IntroductiontoClearingDirectory)

- [Clearing Directory Upload](#ClearingDirectoryUpload)
- [Reachability Check](#ReachabilityCheck)
- [License Codes](#LicenseCodes)

Related topics:

- [Temenos Payment Services](../../Services/Misc/Services.htm#Service_CA)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:14:01 PM IST