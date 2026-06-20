# Introduction to Sri Lanka CITS Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SriLanka/Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Sri Lanka > [Sri Lanka Cheques](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm) > Introduction

- Sri Lanka;)
  - [Sri Lanka Clearing Sri Lanka Clearing](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm)
  - [Sri Lanka Cheques Sri Lanka Cheques](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm)
    - [Introduction](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm)
    - [Configuration](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Configuring.htm)
    - [Working with](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Working_with.htm)
    - [Tasks](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Tasks.htm)
    - [Outputs](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Outputs.htm)
  - [Sri Lanka Interbank Payment System Sri Lanka Interbank Payment System](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm)
  - [Sri Lanka CEFTS Instant CT Payments Sri Lanka CEFTS Instant CT Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm)
  - [Sri Lanka CEFTS Instant DD Payments Sri Lanka CEFTS Instant DD Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm)

Payments

# Introduction to Sri Lanka CITS Clearing

Updated On 08 November 2022 |
 20 Min(s) read

Feedback
Summarize

LankaClear is an operator of Sri Lanka’s National Payment Network, which supports the following by using Cheque Imaging and Truncation System (CITS):

- Incoming and outgoing cheque payments
- Incoming and outgoing return of cleared cheques
- Outgoing cheque representations

CITS is an image-based cheque clearing system, which replaces the physical cheque with electronic information. This helps in reducing the delay associated with the physical movement of cheques and bringing clearing cycle to the next business day (T+ 1 clearing).

LankaClear has enabled the all-participating banks to submit the images and MICR data of physical cheques through a secured virtual private network. This allows the participant banks to upload large volume of cheques (in batches) and initiate their clearing, immediately.

CITS is a net settlement system designed for settlement of cheque payments in Sri Lankan Rupees (LKR) and USD. It uses fixed length cheque files in Text format to send and receive payment messages.

## Types of Messages

The cheque file (LKR) in Text format (Fixed Length File) is downloaded from LankaClear site and uploaded to Temenos Payments Hub. The files types for CITS clearing are as follows:

- Outward cheque presentation sent – OWNMCHQ
- Outward cheque representation sent – OREMCHQ
- Returns received for the outward cheques – INRTCHQ
- Inward cheque clearing file received – INPMCHQ
- Returns sent out for the inward cheques – ONRMCHQ

## Architectural Diagram of LankaClear CITS

The below workflow shows the process of payment between channels and Lanka cheque clearing by using Temenos Payments Hub.



| Item | Description |
| --- | --- |
| Bank Electronic Channels or Aggregators | Used to capture cheque collection request |
| Teller or Cheque Collection Application | Front End Temenos module to manually capture cheque collection request |
| Payment Engine | Payment system from Temenos Payments Hub to process payments |
| CITS Lanka Cheque Clearing | Lanka cheque clearing system |
| Bank’s Host and Supporting Systems | Used for account and cheque number validations, balance checks, and postings |

## Workflow of LankaClear CITS Cheque File

The following are the two types of clearing in LankaClear CITS:

[Outward Clearing](#)

This enables to process the cheque collection of `TELLER` and Central Clearing Department of the bank to upload the data file to Clearing House (LankaClear).



The following are the other bank cheques that are deposited in Temenos Payments Hub bank account:

| Cheque | Description |
| --- | --- |
| Outward Cheque Presentation or Representation | 1. User captures a single or bulk cheque transaction in the Teller page.    - The `TELLER` application validates the creditor account to check for posting restrictions on the account.    - The Teller page performs the cut-off and reachability check. 2. Once a cheque collection record is created in the system, Cheque Collection module invokes an API to create a new transaction in Temenos Payments Hub. 3. Temenos Payments Hub performs the following:    - Processes the transaction according to the standard processing.     It skips Debit Party Determination (DPD), Credit Party Determination (CPD), account validation, date determination, fee determination, posting, as the `TELLER` application:    - Has the account number (already) given by the Operator    - Generates accounting entries before sending the request to the Temenos Payments Hub  - Creates corresponding outgoing Cheque Representation file (OREM) or Cheque Presentation file (OWNM) based on the value in the *Cheque Presentment Type* field in the Teller page) file and sends it to the Lanka Clearing, based on the clearing frequency configuration. |
| Inward Returns | 1. Drawer bank sends a return file for the transaction (outgoing cheque collection file sent to the other bank) that is not processed due to some errors The errors include stop payments and closure of the account. 2. On receiving the return file, Temenos Payments Hub invokes the Cheque Collection API that marks the status of the original transaction as 996.   If the user wants to represent the cheque, a new transaction is created in the `TELLER` application with a value in *Cheque Presentment Type* field of the Teller page. |

[Inward Clearing](#)

This enables to process the inward cheque files received from Clearing House (LankaClear).



The following are the Temenos Payments Hub bank cheques that are deposited in other bank accounts:

| Cheque | Description |
| --- | --- |
| Cheque Presentation or Representation | 1. User maps the inward cheque presentation file (or representation file) received from the Lanka clearing to Temenos Payments Hub internal mapping objects. 2. Temenos Payments Hub validate whether the cheque is already paid (if there is no stop payment of the cheque and sufficient funds are not available in the customer account). 3. On successful validation, it process the payment and generates the accounting entries.   If an error occurs (during processing), it moves the transaction to the Repair queue for the user to manually accept, correct or return the cheque transaction. |
| Outward Returns | 1. User returns the cheque transaction from the Repair queue by choosing the appropriate return code for the transaction. 2. On authorisation, the following happens:    - Return transaction is ready for the outgoing generation    - Return presentation file is generated at the clearing frequency configured and sent to clearing in the acceptable format  3. Temenos Payments Hub generates the reverse accounting, after processing the return. |

## Types of Participants

Temenos Payments Hub supports both direct and indirect participants. It configures the Source, Channel and Clearing settings (separately) based on whether Temenos Payments Hub is a direct or an indirect participant for LankaClear CITS clearing.

## Dates

The Teller module calculates the Credit Value Date (CVD) and Exposure Date according to the configuration and passes the values to Temenos Payments Hub for outward cheque collections.

The Teller module can only setup the bank holidays, hence, it is referred when setting up the cheque collection request initiated from Teller.

## Routing

The bank routes the payment to CITS (Lanka Cheque clearing) based on the routing rule maintained in Temenos Payments Hub. This functionality is also used to route the payment to other suitable channels in a location, when the criteria for LankaClear CITS transfers are not met.

Additionally, if the system misses the cut-off, it routes the payment through another channel according to the configuration in Temenos Payments Hub.

To know more, refer to Routing and Settlement section.

## Charges

The charge type is mapped to SHA for LankaClear CITS transfer in Temenos Payments Hub. This allows in charging the following:

- Processing fees from a Creditor during processing of outward cheque collection files.
- Processing fee from the Customer during processing of Inward cheque collectionfiles.

Temenos Payments Hub allows to setup the standard fee products, which is used to calculate the charges. These charges are configured in the Teller module for cheque collection request. User can waive-off these charges (if required) from the Teller page.

The Teller page does not allow to display, capture or modify the charges.

## Clearing Directory and Reachability

Directory upload is not required for the Lanka cheque clearing, as Teller module handles the reachability check.

If required, a local program can validate for the following:

- Debtor bank BIC is reachable through the Lanka clearing
- Cut-off time is breached in the `TELLER` application (If breached, it moves the value date to the next date).

## Cut-Off Time

The Teller module can handle the cut-off and reachability checks. System validates whether the cheque file is sent to clearing before the cut-off time (that is, 4.30 PM). If the cut-off time has passed, it moves the settlement date to the next business date and the return is sent on the next day. However, it warehouses the payment that is generated after cut-off and has settlement date as next working date.

## Manual Entry of LankaClear CITS Transfers

Cheque collection record creates a transaction in Temenos Payments Hub based on inputs in the front end Teller page. If the system encounter an error during processing, it moves the transaction to the Repair queue for the user to accept and modify the transaction or it is returned. Any inward cheque or return transaction that falls in the Repair queue requires manual intervention to complete the processing.

To know more, refer to the Working with section.

## Outward Clearing File

This section describes the process of an outward cheque clearing deposited in Temenos Payments Hub bank.



| Activity | Description |
| --- | --- |
| Cheque collection request | - Creates a transaction in Temenos Payments Hub based on inputs in the Front End Teller page. - Captures the Credit Account, Cheque Number, Cheque Bank Code and Value Date. |
| Credit account validation | Validates whether the creditor account is a valid Temenos Transact account and does not have any posting restrictions. |
| Reachability check | Validates whether the debtor bank BIC is reachable through the Lanka clearing or cut-off time has breached in the `TELLER` application. If breached, it moves the value date to the next date. |
| Routing | Route the payment to CITS (Lanka Cheque clearing) based on the routing rule maintained in Temenos Payments Hub. |
| Dates calculation | Calculates the following dates: |
| Duplicate check | Configures the check based on bank, branch, cheque number, and credit value date for outgoing cheque collection transaction. |
| Filtering | Filters the payment when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. |
| Fees calculation | Charges processing fees from a creditor. The user cannot waive-off the fees from the Teller, when capturing the cheque collection request. |
| Posting | Configures the transaction as ‘Pre-Settled’ in Temenos Payments Hub. It performs the following:  - Credits the creditor’s account with the transaction amount that has future exposure date. - Debits the charges (if any) from the creditor account.  The following posting is done for a cheque collection request:  - Debit clearing suspense account - Credit creditor account (with future exposure date)   **Settlement Booking Entry**  Creates and posts a separate settlement transaction for moving funds between the clearing nostro and suspense accounts, after generating the file.   - Debit nostro account - Credit outward clearing suspense account   Auto-posting of settlement entries is supported only with PH license. |
| Update cheque collection module | Updates the cheque status in Cheque Collection module to set the cheque status as ‘Deposited’. |
| Generate and send outward files to clearing | - Generates a Lanka file by bulking all cheque collection requests. - Sends the USD drafts as a separate file to clearing. The file submission happens at pre-defined clearing schedule. - Sends a unique 25-digit transfer reference in the outgoing file of Lanka Cheque Clear Transfers. The logic for the 25 digit identifier is as follows:   - Current Business Date + Bank Code (`PP.COMPANY.PROPERTIES` for the Current Processing Company+ Branch Code+ Batch Number+XXXX)   where  XXXX denotes the Running serial number to be generated by the system starting as “0001” |
| Error queue | Routes the validation error (of cheque collection transaction) to the Repair queue for manual intervention. The validation error for outward cheques is due to an incorrect product or clearing configuration in Temenos Payments Hub. |

[Cancellation of Outward Cheque](#)

User selects the transaction from ‘Awaiting to Send to Clearing’ queue and cancels it.



| Activity | Description |
| --- | --- |
| Selecting the transaction for cancellation | User navigates to the enquiry and selects the transaction for cancellation. |
| Check for status | - Changes the status of the transaction to ‘Returned’ and ‘Cancelled’, and updates the cheque collection record, accordingly. - Changes the status of cheque collection record from ‘Deposited’ to ‘Returned’. - Updates the audit trails on the record as ‘Outward Cheque Collection – Cancelled based on User’s Input’. |
| Settlement | Reserves the accounting entries at the Teller module. |

## Inward Returns

This section describes the processing of an inward cheque returns in Temenos Payments Hub bank.



| Activity | Description |
| --- | --- |
| Receiving the return file | Receives the return cheque processing file and maps it.  Identifies the original transaction based on the transaction reference, and marks it as Returned. |
| Reverse the settlement entries | Reserves the original entries as follows:  - Debit Original Credit or Original Suspense Account - Credit Return Suspense Account Reverses the settlement accounting (raised when sending the file) on receiving the return file. It is raised automatically for PH license. - Credit Nostro Account - Debit Return Suspense Account |
| Identify the original transaction | Identifies the original transaction with reference and updates the status as 996 (Completed with Return) If there are no matches, the user can manually change it. |
| Update the cheque collection | Updates the cheque collection status as ‘Returned’. |

## Inward Clearing File

This section describes the process of an inward cheque clearing received by Temenos Payments Hub.

.

| Activity | Description |
| --- | --- |
| Message acceptance | Validates the received file |
| Message mapping | Debulks and maps the Lanka clear file and creates a cheque clearing transaction. |
| Enrich the cheque type to be stored in Temenos Payments Hub | Clearing specific enrich API fetches the cheque type based on account number and stores it in Temenos Payments Hub. It does not map the cheque type to Temenos Payments Hub and places the transaction in the Repair queue for manual action, when:  - Multiple cheque types are linked to a particular account - Account is not available or invalid |
| Debit account validation | Validates whether debit account is valid, active and does not have any posting restrictions. |
| Manual verification | Processes the cheque clearing transaction as an automated (Straight-Through Processing - STP) or manual process (non-STP). If it is non-STP, the system parks the payment in Manual queue for manual action by the Operator (image or signature verification and other manual process).   - After manual verification, the user can release the payment for STP processing. - If not, all payments are released (Scheduled Release) based on a configured cut-off time. |
| Cheque number validation | Validates the cheque details against Cheque Register. - It processes the payments, when the cheque status is ‘Issued’. - If the status is ‘Returned’, it generates a warning to the user for overriding and continuing with the represented cheque. |
| Balance check | Checks for sufficient funds in the debtor’s account before posting an inward cheque. If funds are available, it performs the fund reservation. If the bank skips the balance check, the following happens:  - Cheques with insufficient funds are overdrawn - Changes payment status to ‘Completed’ - Marks the cheque as ‘Cleared’ However, the bank can manually return the cleared cheque before generating the Return File and sending it to clearing. |
| Dates calculation | Performs dates calculation for debit value date according to the configuration in Temenos Payments Hub. |
| Duplicate check | Checks the cheque clearing transaction based on the below attributes (if configured):  - Sending bank - Branch code - Cheque number - Value date   The fields used for duplicate check is configured based on the client requirements. |
| Filtering | Filters the payment when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. |
| Charge calculation | Charges the required fee (from the customer) based on the configuration in the fee product. The calculated fee is applied on the customer’s account during posting. |
| Posting | Debits the debtor’s account with the transaction amount.  - Debit Debtor’s Account - Credit Clearing Suspense Account   **Settlement Booking Entry**  System creates and posts a separate clearing settlement transaction moving the funds between the cheque clearing nostro and clearing suspense account, when the inward file is processed.   - Debit  Clearing Suspense Account - Credit Nostro Account   It supports auto-posting of settlement entries with PH license. |
| Update cheque status | Updates the cheque status in Temenos Transact Cheque Register as ‘Cleared’. |
| Repair | If an error while processing an inward cheque clearing, it routes the transaction to the Repair queue for manual intervention or system automatically rejects it (based on configuration). User performs the following:  - Repairs the transaction in the Repair page by changing the account and cheque numbers. - Resubmits or returns the transaction (manually) with a specific return reason code.   - It allows automatic return processing only when Temenos Payments Hub (PH) license is available. - It modifies the cheque number in the Repair page before proceeding with the inward cheque payment. |

## Outward Returns

This section describes the processing of outward cheque returns in Temenos Payments Hub bank.



| Activity | Description |
| --- | --- |
| Return Initiation | Initiates after receiving an inward cheque when the clearing fails (during processing). |
| Routing | Routes a return payment to clearing channel (according to the original channel). |
| Clearing Cut-Off Time Check | Validates whether the cheque clearing cut-off has passed. If passed, it moves the settlement date to the next business date and sends the return on the next day. |
| Fee Calculation | Collects the fees from the customer when processing of cheque clearing transaction is unsuccessful. Calculates the fee based on the Fee Products configured in Temenos Payments Hub. |
| Posting | The following entries are posted against the original cheque clearing transaction:  - Debit Returns Suspense Account - Credit Cheque Clearing Suspense Account  The following entries are posted against the return transaction:  - Debit Cheque Clearing Suspense Account - Credit Return Suspense Account |
| Mark original Payment as Returned | Marks the original cheque clearing transaction as ‘Returned’ and updates the cheque status as ‘Returned’ in Temenos Transact. |
| Generate Return message | Generates an outward return file and forwards it to clearing by bulking all the processed return transaction. The file is sent to clearing at the pre-defined clearing schedule (based on clearing frequency configuration). It marks the Return Transaction status as ‘Completed’. |
| Repair | If an error occurs in the return transaction, it routes the transaction to the Repair queue for manual intervention. |

## CITS Incoming File Validation

This functionality allows banks to handle the validation on the incoming clearing file for incoming debit and incoming return received from Cheque Imaging and Truncation System (CITS) clearing, on the record length (per transaction). The length of every record received in the incoming debit file needs to be 80 chars and, for the incoming return file, it needs to be 199 chars in length. If any record length is not 80 or 199, then the entire file will be rejected and, the appropriate error code and description will be logged in the system for that file.

## Illustrating Model Parameters

To know more on parameter setup for Cheques and Cheque Returns, refer the [Payment Hub (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm), [Payment Suite (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

PPLCIT module provides facility to initiate and receive Cheque requests through CITS Clearing.

In this topic

- [Introduction to Sri Lanka CITS Clearing](#IntroductiontoSriLankaCITSClearing)

- [Types of Messages](#TypesofMessages)
- [Architectural Diagram of LankaClear CITS](#ArchitecturalDiagramofLankaClearCITS)
- [Workflow of LankaClear CITS Cheque File](#WorkflowofLankaClearCITSChequeFile)
- [Types of Participants](#TypesofParticipants)
- [Dates](#Dates)
- [Routing](#Routing)
- [Charges](#Charges)
- [Clearing Directory and Reachability](#ClearingDirectoryandReachability)
- [Cut-Off Time](#CutOffTime)
- [Manual Entry of LankaClear CITS Transfers](#ManualEntryofLankaClearCITSTransfers)
- [Outward Clearing File](#OutwardClearingFile)
- [Inward Returns](#InwardReturns)
- [Inward Clearing File](#InwardClearingFile)
- [Outward Returns](#OutwardReturns)
- [CITS Incoming File Validation](#CITSIncomingFileValidation)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Installation Guide](https://docs.temenos.com/docs/Solutions/Installation/SriLankaMB_InstallationGuide/CountryModelBank/SriLanka/PPLCIT/Installation.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:44:10 PM IST