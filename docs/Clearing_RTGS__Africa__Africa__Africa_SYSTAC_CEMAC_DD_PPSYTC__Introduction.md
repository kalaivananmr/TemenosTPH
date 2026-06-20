# Introduction to SYSTAC Direct Debit

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm) > Introduction

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
    - [Introduction](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
    - [Configuration](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Configuration.htm)
    - [Working with](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Working_with.htm)
    - [Tasks](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Tasks.htm)
    - [Outputs](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Outputs.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Introduction to SYSTAC Direct Debit

Updated On 22 March 2025 |
 17 Min(s) read

Feedback
Summarize

Système de Télécompensation en Afrique Centrale (SYSTAC) is a net, secure, and automated system that processes large volume of non-emergency debit and credit transactions (credit transfers and cheques) with a unit amount of less than CFA 100 million. It has the following objectives in Central Africa:

- Fast processing of transactions in accordance to Bank of Central African States (BEAC) and international standards
- Reducing risks associated to payment transactions
- Facilitating monetary management and functioning of the financial market
- Making exchanges at national and sub-regional level

Additionally, SYSTAC is dedicated to clearing financial flows at the regional level (CEMAC).

## SYSTAC Participants

BEAC provides the participant’s details to each bank, and when there is change in the participant repository, it generates a new file and circulates to all participants. The text file consists of the following details:

- Banks in CEMAC region with bank codes (banque.txt)
- Branches of banks in the above file (agence.txt)

[Types of Direct Debits](#)

The following are the types of direct debits:

| Type of Direct Debit | Description |
| --- | --- |
| Outward DDs | - Initiates outward DD   - Manual capture of DD mandates   - Generation of claims at a pre-defined frequency - Supports cancellation of outward DDs before the generation of the outward file - Processes the reject of outward DDs received from other banks - Supports cancellation of reject of outward DDs by the other banks (customised during implementation) |
| Inward DDs | - Processes the received file that has inward DDs - Rejects the inward DDs - Receipt of cancellation of inward DD (customised during implementation) - Cancellation of reject of inward DDs (customised during implementation) |

[Cut-Off Time](#)

BEAC has a cut-off time of 11.45 hours for interbank DDs, within which banks can send or receive files.

[Value Dates](#)

The following are the value dates for outing and incoming DDs:

| Type of DD | Date | Calculation |
| --- | --- | --- |
| Outgoing | Debit Value Date | D+1 working day |
| Credit Value Date | D+2 working day |
| Processing Date | D day |
| Incoming | Debit Value Date | U |
| Credit Value Date | D day |
| Processing Date | D day |

## File Naming Convention

The naming conventions of the file for SYSTAC clearing is as follows:

| DD Type | Naming Convention | Description |
| --- | --- | --- |
| Outward DD | 01-cc-xxxxx-dddddddd-hhhhhh-20-21-950.ENV | - cc − Country code - xxxxx − Remitting participant code - dddddddd − File generated date (in DDMMYYYY format) - hhhhhh − File generated time (in HHMMSS format) - The rest are constants |
| Rejection of inward DD | 01-cc-xxxxx-dddddddd-hhhhhh-20-22-950.ENV | - cc − Country code - xxxxx − Remitting participant code - dddddddd − File generated date (in DDMMYYYY format) - hhhhhh − File generated time (in HHMMSS format) - The rest are constants |

## Clearing Files Supported

SYSTAC supports the following clearing files:

| Clearing File | Description |
| --- | --- |
| ENV (20-21) | Outward DD collections |
| ENV (20-22) | Outward reject |
| RCP (20-21) | Inward DD collections |
| RCP (20-22) | Inward reject |
| ENV (23-21) | Outward DD collections (resubmitted) |
| ENV (23-22) | Outward reject (resubmitted) |
| RCP (23-21) | Inward DD collections (resubmitted) |
| RCP (23-22) | Inward reject (resubmitted) |

## Business Validations

System performs the following business validations on the debit account when an inward DD is received:

- RIB validation
- Account closed
- Dormancy or inactive
- Posting restrictions
- Account currency

## RIB Validation

The clearing supports Relevé d'identité bancaire (RIB) to address the beneficiary account. The following validation is performed on the RIB of the debtor:

- Number of characters needs to be 23

RIB consists of the following:

- Beneficiary bank code (5 characters)
- Beneficiary bank’s branch code (5 characters)
- Beneficiary account number (11 characters)
- Control digits (2 characters)

Control digit needs to conform to the following algorithm. The RIB key is a mathematical formula, which can only be applied to numeric values. Therefore, any letters available in the data of the RIB needs to be replaced before calculating the key.

Each letter is replaced by its numerical equivalent:

- A, J = 1
- B, K, S = 2
- C, L, T = 3
- D, M, U = 4
- E, N, V = 5
- F, O, W = 6
- G, P, X = 7
- H, Q, Y = 8
- I, R, Z = 9

The key (control digits) can then be calculated with the following formula:



## Reject Reason or Status Codes

All transactions are assigned pre-configured codes to identify the current status of the transaction. These status codes cannot be amended. Reject reason codes are configured and linked to the error codes.

The clearing reject codes required to suit the banks’ business needs is as follows:

| Clearing Reject Code | Reject Code Description |
| --- | --- |
| 04 | Opposition or rejection |
| 05 | Unidentifiable claim |
| 11 | Insufficient funds |
| 13 | Closed account |
| 17 | Amount contested |
| 21 | Contested deadline |
| 34 | Wrong authorisation number |
| 36 | Unusable bank details |
| 39 | Destination client not recognised |
| 42 | No order to pay |
| 43 | Value already set |
| 51 | No provision |
| 54 | Due date not past |
| 56 | Blocked account |
| 57 | Client dead |

## Message Flow Diagram

[Outward DD](#)

The below workflow diagram shows the capture or initiation of DD and its flow to settle it through SYSTAC clearing. It also shows the payment message flow from mandate capture till BEAC system.

 Clearing_Direct Debit/Introduction to SYSTAC Direct.png)

[Inward DD](#)

The below workflow diagram shows the receiving and uploading of the inward files received from BEAC system that processes the transactions.

 Clearing_Direct Debit/Introduction to SYSTAC Direct_1.png)

The local solution is as follows:

- Cancellation received together with inward DD can mark the inward DDs that are cancelled and generate the DDs that are not cancelled.
- Cancellation received subsequently can generate cancellation files

## Processing Workflow

[Outward DD](#)

 Clearing_Direct Debit/Introduction to SYSTAC Direct_2.png)

| Actions | Description |
| --- | --- |
| Manual capture | Captures mandate details to generate outward DD directly in Order Entry (OE) or DD.DDI page (if Temenos Transact core banking system). On the DD.DDI page, the user can captures mandate in which DDs are t generated at a pre-defined frequency. System automatically generates the DD on the scheduled date. Validates mandatory fields on submission. |
| Account validations | Performs the following validations on the ordering customer account (debit account):  - Account closed - Dormancy or inactive - Posting restrictions - DD currency |
| Destination or debtor bank code validations | Validates whether the value in destination or debtor bank is a valid participant bank code from the list circulated by BEAC. |
| Business validations | BEAC accepts only RIB for customer accounts, which consists of the following:  - Bank code (5 characters) - Branch code (5 characters) - Account number of beneficiary (11 characters) - Control digits (2 characters)  Validates the debtor’s account for the following:  - Checks the total number of characters (23) - Calculates the ‘clé RIB’ depending on data input and checks data bank code, branch code and account number   Transaction currency needs to be the local currency. |
| Transaction limit | Specifies the maximum amount that can be configured |
| Reachability check | Performs the check on debtor’s bank at the transaction level against the Clearing Directory. Recipient of the outward file is always BEAC. |
| Submission and supervisor approval | Performs the following actions:  1. On submission of the mandate, it waits for Supervisor’s approval. 2. Once approved, it is moved for further processing.    - If the supervisor rejects, the record is modified and resubmitted for approval. 3. It generates the DD on the scheduled date and Temenos Payments Hub Engine consumes it for further processing. |
| Warehouse | Warehouses DD with future processing date and releases it on Start of Day (SOD) of the processing date. It changes (automatically) and warehouses the processing date (in the DD) initiated after the cut-off time to the next working day (D+1). |
| Filtering | Supports external screening of financial crime and other compliance checks through an interface (which is developed locally). TPH solution is pre-integrated with Temenos Financial Crime Mitigation (FCM) solution. |
| Routing | Routes DD to a SYSTAC clearing channel |
| Dates calculation | Calculates the dates (automatically) based on the configuration |
| Fee calculation | Configures commission or fee (if applicable), and collects it when generating accounting entries for the transaction |
| Duplicate check | Performs duplicate check during processing and generates an error (if any) |
| Posting | Generates settlement entries (automatically) after the reject cut-off time. |
| Channel validations | Performs all validations on the DD to ensure compliance requirements of SYSTAC |
| File generation | Generates outward DD file at the scheduled frequencies (till the clearing cut-off) and places it in the pre-defined directory |
| Repair queue | Displays an error when processing the payment. It moves the transaction to Repair queue for the user to accept, modify or cancel. |

When the system rejects DD collection in TPH and the DD module receives a notification of the rejection, it automatically creates, accepts, authorises, or moves the DD.RETURN record to an Exception queue for investigation. The return reason codes defined in the *Hold Reason Code* field of DD.CODES is used to authorise (manually or automatically) the record. The user can accept and authorise the return record from the Exception queue for creating the return accounting entries. After authorising the DD.RETURN record (manually or automatically) for the reject of outward DD collection, the system updates the *Resub Val Date* field based on the configuration in *Resub Date Prd* field of DD.PARAMETER.

- If a return reason code is defined in the *Resubmit Excl Code* field of DD.CODES, the *Resub Val Date* field is not updated. Hence, the user cannot resubmit the DD for this reject reason code.
- If not set in DD.PARAMETER, the system allows the user to enter the resubmission date (a future date) in DD.RETURN during manual authorisation of the return record on rejection.

DD module generates the resubmission of DD to TPH on the scheduled date for further processing. Clearing nature code of POR.TRANSACTION is updated with value ‘REP’ to indicate that it is a resubmitted DD collection. Although, the processing of the resubmitted DD collection is similar to initial DD collection, a separate file is generated for the requirements in clearing.

[Cancellation of Outward DD before Distribution to Clearing](#)

All the outward DD instructions with pending to be distributed to clearing are listed in an enquiry with an option to cancel. On cancellation, it marks the original record as cancelled and removes it from the ‘out’ file queue.

 Clearing_Direct Debit/Introduction to SYSTAC Direct_3.png)

| Activity | Description |
| --- | --- |
| Identify the original transaction | Select the transaction that needs to be cancelled from the list of outward DDs (for a specific date) displayed in an enquiry |
| Mark reversal | Marks the transaction as cancelled |
| ‘Out’ file | Record is removed from the ‘out’ file queue |

Cancellation of outward DD after distribution to clearing is to be handled locally.

[Reject of Outward DD](#)

When the system receives the outward DD reject files (20-22.RCP and 23-22.RCP) from SYSTAC, it maps the inward files for identifying the original transaction and marks them as ‘Rejected’. This allows to automatically create a reject transaction and complete the rejection process.

 Clearing_Direct Debit/Introduction to SYSTAC Direct_4.png)

| Action | Description |
| --- | --- |
| Receive and map | Reject of outward DD file (20-22.RCP) is received and mapped. |
| Identify original transaction | Outward DD transactions that are rejected are identified. |
| Mark original transaction | Original transaction is marked as rejected. |
| Create reject transaction | Reject transaction is created. |
| Complete reject transaction | Reject transaction is completed. |

[Cancellation of Reject of Outward DD](#)

When a reject of outward transfer (20-22.RCP) file is received, it is kept in pending state till the cut-off time for the receipt of cancellation (if any). When the cancellation of reject of outward transfer (10-24.RCP) file is received, it marks the outward transfers that are rejected but are subsequently cancelled. The file with these outward transfers that are rejected but not cancelled (20-22.RCP) are loaded into TPH.

This requirement needs to be handled locally.

[Inward DD](#)

When the system receives the inward clearing files (20-21.RCP and 23-21.RCP) with inward DD collections from SYSTAC, it accepts and maps them for processing. All inward DDs (including resubmitted DDs) are processed as STP. When the system encounters any errors, it moves the transactions to the Repair queue.

The below workflow diagram shows the process for the inward handling in TPH.

 Clearing_Direct Debit/Introduction to SYSTAC Direct_5.png)

| Action | Description |
| --- | --- |
| Inward DD file | Uses the inward DD file (automatically) received for processing |
| Account validation | Performs the following validations for debtor’s account (credit account):  - Account closed - Dormancy or inactive - Posting restrictions - DD currency |
| Dates calculation | Calculates the dates for processing |
| Filtering | Supports any external screening for financial crime and other compliance checks through an interface, which is developed locally. TPH is pre-integrated with Temenos FCM solution. |
| Fee calculation | Configures the commission or fee (if applicable) for DD and collects it when generating the accounting entries for the transaction. |
| Duplicate check | Configure duplicate check during the processing of the DD and generates an error (if any) |
| Debit posting | Credits the debtor’s account on successful completion. If an error occurs, it places the DD in the Repair queue. |
| Repair queue | If an error occurs while processing, it moves the transaction to Repair queue for the user to accept, modify or reject the DD. |

[Cancellation of Inward DD](#)

When an inward transfer file is received, it is kept in waiting state till the cut-off time. When the cancellation of inward transfer file is received, it removes all the inward transfers that are cancelled. The file with inward transfers that are not cancelled is generated after cut-off time and sent to TPH for processing.

This requirement needs to be handled locally.

[Reject of inward DD](#)

When the system encounters any errors while processing inward DDs (including resubmitted items), it moves the records to the Repair queue. The user can access and reject these records after providing the reject reason code. The system places the transactions in the Out File queue to generate reject of inward DD files (20-21.ENV and 23-21.ENV) at clearing frequency.

 Clearing_Direct Debit/Introduction to SYSTAC Direct_6.png)

| Action | Description |
| --- | --- |
| Initiate reject of inward DD | Initiates the reject (reject) of inward DD from the Repair queue |
| Mark reject | Marks the transaction as rejected |
| Place in ‘Out’ file queue | Places the transaction in Out queue of ‘Reject of inward DD’ |
| Generate Out file | Generates ‘Reject of inward DD’ file (20-22.ENV) |

[Cancellation of Reject of Inward DD before Distribution to Clearing](#)

An enquiry lists all the reject of inward transfers which are pending to be sent back to clearing. Cancellation of reject of inward transfers can be initiated and once completed, the record is deleted from ‘out’ file queue for the generation of file. The original inward transfer is placed in the Repair queue from where the user can accept.

 Clearing_Direct Debit/Introduction to SYSTAC Direct_7.png)

| Action | Description |
| --- | --- |
| Identify transaction | Identifies the reject of inward DD transaction and cancels it in the enquiry list |
| Mark reversal | Marks the reversal of reject in the transactions |
| Transaction placed in repair queue | Places the inward DD transaction in the Repair queue. |
| Transaction removed from Out file | Removes the transaction from the Out file queue with ‘Reject of inward DD’ (20-22.ENV) |
| Completion of inward DD processing | Access and accept the inward DD transaction from the Repair queue To know more, refer to Inward DD Processing section. |

Cancellation of reject of inward DD after the generation of the file is to be handled locally.

## Illustrating Model Parameters

Read the [Temenos Payment (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Suite (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) user guides for information on parameter setup for CT, DD and Returns.

## Illustrating Model Products

This module provides facility to initiate and receive DD requests through SYSTAC Clearing.

In this topic

- [Introduction to SYSTAC Direct Debit](#IntroductiontoSYSTACDirectDebit)

- [SYSTAC Participants](#SYSTACParticipants)
- [File Naming Convention](#FileNamingConvention)
- [Clearing Files Supported](#ClearingFilesSupported)
- [Business Validations](#BusinessValidations)
- [RIB Validation](#RIBValidation)
- [Reject Reason or Status Codes](#RejectReasonorStatusCodes)
- [Message Flow Diagram](#MessageFlowDiagram)
- [Processing Workflow](#ProcessingWorkflow)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:33:55 PM IST