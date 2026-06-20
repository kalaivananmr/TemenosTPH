# Introduction to SYSTAC (CEMAC) Credit Transfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm) > Introduction

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
    - [Introduction](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
    - [Configuration](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Configuration.htm)
    - [Working with](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Working_with.htm)
    - [Tasks](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Tasks.htm)
    - [Outputs](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Outputs.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Introduction to SYSTAC (CEMAC) Credit Transfer

Updated On 08 November 2022 |
 14 Min(s) read

Feedback
Summarize

The Système de Télécompensation en Afrique Centrale (SYSTAC) is a net, secure and automated system that processes large volume of non-emergency debit and credit transactions (credit transfers and cheques) with a unit amount of less than CFA 100 million. It has the following objectives in Central Africa:

- Fast processing of transactions in accordance to Bank of Central African States (BEAC) and international standards
- Reducing risks associated to payment transactions
- Facilitating monetary management and functioning of the financial market
- Making exchanges at national and sub-regional level

Additionally, SYSTAC is dedicated to clearing financial flows at the regional level (CEMAC).

## SYSTAC Participants

BEAC provides the list of participating banks in their clearing to each bank. If there is change in the participant repository, BEAC generates and sends a new file with all the details (not only the deltas). The text file consists of the following details:

- Banks in CEMAC region with bank codes (banque.txt)
- Branches of banks in the above file (agence.txt)

## Types of Credit Transfers

The following are the types of credit transfers:

| Type of Credit Transfer | Description |
| --- | --- |
| Outward | - Initiates outward transfers   - Capturing the transfers (manually)   - Setting up standing instructions to generate the transfer at a pre-defined frequency   - Processing the request received through MT101   - Processing the file received from the customer containing credit transfers or online tax payment - Cancels the outward transfers before and after the generation of file (to the clearing) - Processes return of outward transfer received from other banks - Cancels the return of outward transfer by other banks |
| Inward | - Processes the received file that has inward transfers - Returns the inward transfers - Processes the cancellation of inward transfer |

## File Types Supported

SYSTAC supports the following clearing files:

| Clearing File | Description |
| --- | --- |
| 10-21.ENV | Outward transfer |
| 10-22.ENV | Inward return |
| 10-21.RCP | Inward transfer |
| 10-22.RCP | Outward return |
| .RJT | Clearing reject |

## Cut-Off Time

BEAC has a cut-off time of 11.45 for interbank transfers, within which banks can send files.

## Value Date

The following are the value dates for outing and incoming transfers:

| Type of CT | Date | Calculation |
| --- | --- | --- |
| Outgoing | Debit Value Date | D–1 working day |
| Credit Value Date | D day |
| Processing Date | D day |
| Incoming | Credit Value Date | D+1 working day |
| Debit Value Date | D day |
| Processing Date | D day |

## Message Workflow Diagram

This section displays the workflow diagram of outward and inward transfers.

[Outward Transfer](#)

 Clearing_Credit Transfer/Introduction to SYSTAC Credit.png)

[Inward Transfer](#)

 Clearing_Credit Transfer/Introduction to SYSTAC Credit_1.png)

The local solution is as follows:

- Cancellation file received together with inward transfer file can:
  - Mark the inward transfers that are cancelled
  - Generate inward transfer file for transfers that are not cancelled
- Cancellation file received subsequent to the inward transfer file can generate and send the files to TPH for processing.

## Outward Processing

Outward transfer can be initiated through Payment Order or bulk file upload (where the file is mapped to TPH neutral format before upload). Standing order can also be setup for the transfers. On the execution date, payment order is created, and outward transfer is requested through MT101.

 Clearing_Credit Transfer/Introduction to SYSTAC Credit_2.png)

| Actions | Description |
| --- | --- |
| Manual capture | Captures outward transfer in `PO` application page.  - Sets the standing instructions for regular transfers at pre-defined frequency - Validates the mandatory fields on submission |
| Bulk file upload or MT101 | Performs bulk file upload to create transactions directly in TPH. It directly processes the request for transfer received through MT101 in TPH. |
| Account validations | Performs the following validations on the ordering customer account (debit account):  - Account closed - Dormancy or inactive - Posting restrictions - Availability of funds - Transfer currency |
| Bank code validations | Validates whether the value in beneficiary bank is a valid participant bank code from the list circulated by BEAC. |
| Business validations | Ensures the transaction currency is the local currency (XAF). BEAC accepts only RIB for customer accounts, which involves:  - Bank code (5 characters) - Branch code (5 characters) - Account number of beneficiary (11 characters) - Control digits (2 characters)  The validation of beneficiary account is as follows:  - Checks the total number of characters (maximum 23 characters) - Calculates the ‘clé RIB’ depending on data input and checks data bank code, branch code and account number |
| Transaction limit | Defines the maximum amount allowed for each transfer |
| Reachability check | Checks whether beneficiary bank performs reachability at transaction level. The recipient of the outward file is BEAC. |
| Balance reservation | Validates whether the debit account has sufficient funds to process the payment. If available, it reserves the funds. If not, it cancels the fund (automatically). This solution supports the configuration to address the banks business need. |
| Submission and supervisor approval | Performs the following actions:  1. On submission of the payment, it waits for Supervisor’s approval. 2. Once approved, payment is moved for further processing.    - If the Supervisor rejects the payment, it is modified and resubmitted for approval.  3. Payment is then sent to TPH engine for further processing.   System can be configured to auto-approve, hence, it can be sent to the Payments Engine and processed STP. |
| Warehouse | Warehouses the transfer with future processing date. These transfers are then released at Start of Day (SOD) of the processing date. Processing date in the transfers initiated after the cut-off time is automatically changed to next working day (D+1) and warehoused. |
| Filtering | Supports external screening for financial crime and other compliance checks through an interface (which is developed locally). TPH solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the transfer to a clearing channel (SYSTAC) |
| Dates calculation | Calculates the debit value date as ‘D-1’ and other dates as system date (D). |
| Fee calculation | Configures the commission and applicable fee for the transfer (which is collected when accounting entries are generated for the transaction). |
| Duplicate check | Enables to configure the check when processing the transfer. It generates an error, when the duplicate conditions are met. |
| Posting | Debits the ordering customer’s account on successful completion of the transfer and credits it to clearing suspense account.  - Debit customer - Credit clearing suspense |
| Channel validations | Performs validation on the transfer to ensure compliance requirements of SYSTAC. The following are the standard validations:  - RIB - Account - Currency - Cut-off time |
| File generation | Generates outward files at cut-off and places it in the pre-defined directory. |
| Repair queue | If an error occurs during processing, it moves the transaction to Repair queue for the user to accept, modify or cancel the transfer. |

[Cancellation of Outward Transfer (before Distribution to Clearing)](#)

Banks can initiate cancellation (based on request) for all outward transfer before forwarding it to clearing. An enquiry is provided to list all the transactions, and the user can enable reversal of payment before the file is generated. TPH generates reversal of accounting entries and changes the status of the payment record as ‘Cancelled’. The record is removed from the out file queue that awaits generation of outward file.

 Clearing_Credit Transfer/Introduction to SYSTAC Credit_3.png)

| Activity | Description |
| --- | --- |
| Identify the original transaction | All the outward transfers of data in an enquiry The user needs to modify the transaction that is ‘Cancelled’. |
| Mark reversal | Marks the transaction as cancelled |
| Credit posting | Generated accounting entries to credit the customer’s account  - Debit clearing suspense - Credit customer |
| Out file queue | Removes transaction from ‘Out’ queue file that has outward transfers. |

[Return of Outward Transfer](#)

When a return of outward transfer file is received from the clearing, TPH identifies the original transaction and updates the status accordingly. System creates a return transaction defaulting the values from the original transaction, updates the reject code and completes the transaction.

 Clearing_Credit Transfer/Introduction to SYSTAC Credit_4.png)

| Activity | Description |
| --- | --- |
| Receive and map | Receives and maps the return of outward transfer file (10-22.RCP)  It generates the following accounting entries:  - Debit clearing Nostro - Credit return suspense |
| Identify original transaction | On receiving the return of outward transfer file, the system identifies the original transaction based on the unique reference number linked to the payment. This is available in ‘SendersReferenceOutgoing’. |
| Mark original transaction | Marks the original transaction as ‘Returned’. It generates the following accounting entries:  - Debit clearing suspense - Credit customer |
| Create return transaction | Creates and completes the return transaction  It generates the following accounting entries:  - Debit return suspense - Credit clearing suspense |

[Cancellation of Return of Outward Transfer](#)

When a return of outward transfer (10-22.RCP) file is received, it is kept till the cut-off time of the cancellation (if any). On receiving the cancellation of return of outward transfer (10-24.RCP) file, the following happens:

- Marks the outward transfers returned but are subsequently cancelled
- Loads the file with outward transfers that are returned but not cancelled (10-22.RCP)

This feature needs to be developed locally at the time of implementation.

## Inward Processing

When an inward transfer file is received, it is kept in waiting status till the cut-off time. On receiving the cancellation of inward transfer, the following happens:

- Removes all the inward transfers that are cancelled
- Generates and sends the files with inward transfers that are not cancelled (after cut-off)

  This requirement needs to be handled locally.
- Loads and maps the files with inward transfers
- Processes all the inward transfers in STP (subjecting to validations)

  If an error occurs, it moves the payment to the Repair queue.

The requirement of validation on ‘Name conformity’ is a L3 customisation.

 Clearing_Credit Transfer/Introduction to SYSTAC Credit_5.png)

| Actions | Description |
| --- | --- |
| Inward transfer file | Takes the received inward transfer file (automatically) for processing. It generates the following accounting entries:  - Debit Clearing Nostro - Credit Clearing Suspense |
| Account validation | Performs the following validations in the beneficiary account (credit account):  - Account closed - Dormancy or inactive - Posting restrictions - Transfer currency |
| Dates calculation | Calculates the credit value date as ‘D+1’ and other dates as system date (D). |
| Filtering | Supports any external screening for financial crime and other compliance checks through an interface This needs to be developed locally. Temenos Payments Hub (TPH) is pre-integrated with Temenos FCM solution. |
| Fee calculation | Configures the commission or applicable fee for a transfer (which is collected when generating accounting entries for the transaction) |
| Duplicate check | Performs the validation when processing the transfer. It generates an error, when the duplicate conditions are met. |
| Credit posting | Credits the beneficiary’s account on successful completion of the transfer. It generates the following accounting entries:  - Debit clearing suspense - Credit customer   If an error occurs, it moves the transfer to the Repair queue. |
| Repair queue | If an error occurs during processing, it moves the transaction to Repair queue for the user to accept, modify or return the transfer. |

[Cancellation of Inward Transfer](#)

When an inward transfer file is received, it is kept in waiting status till the cut-off time. On receiving the cancellation of inward transfer file, the following happens:

- Removes all the inward transfers that are cancelled
- Generates and sends the file with inward transfers that are not cancelled after the cut-off

  This requirement needs to be handled locally.

[Return of Inward Transfer](#)

All inward transfer that have encountered errors are placed in the Repair queue. The user needs to take these transfers and complete the return of the transaction.

 Clearing_Credit Transfer/Introduction to SYSTAC Credit_6.png)

| Actions | Description |
| --- | --- |
| Initiate return of inward transfer | Initiates the return (reject) of inward transfer from the Repair queue. |
| Mark return | Marks the transaction as ‘Returned’ and ‘Completed’. It generates the following accounting entries:  - Debit clearing suspense - Credit return suspense |
| Place in ‘Out’ queue | Places the transaction in ‘Out’ queue of ‘Return of inward transfer’. |
| Generate ‘Out’ file | Generates ‘Return of Inward Transfer’ file (10-22.ENV) at the scheduled time. It generates the following accounting entries:  - Debit return suspense - Credit clearing Nostro |

[Cancellation of Return of Inward Transfer before Generation of Return File](#)

This enquiry lists all the return of inward transfers that are pending to be sent to clearing. An option is available to initiate their cancellation, and once completed, the records are deleted from pending queue to generate the files. The original inward transfer is placed in the Repair queue for the user to accept it.

When the user submits a record, the system checks the clearing transaction type to confirm whether ‘RT’ has executed the following:

- Updates the status of return transaction to 997
- Generates the following reversal entries:
  - Debit clearing suspense
  - Credit return suspense

- Maintains audit trail with the name of the user, time stamp and event description as ‘Transaction cancelled before distribution to clearing’.
- Deletes the record from the Pending queue to generate the return of inward transfer file.
- Updates the status of original (inward transfer) transaction to 235. Also, the proposed new error code (informative). It generates the following reversal entries:
  - Debit return suspense
  - Credit clearing suspense
- Maintains audit trail with the name of the user, time stamp and event description as ‘Return transaction cancelled before distribution to clearing’ in the original (inward transfer) transaction.

In this topic

- [Introduction to SYSTAC (CEMAC) Credit Transfer](#IntroductiontoSYSTACCEMACCreditTransfer)

- [SYSTAC Participants](#SYSTACParticipants)
- [Types of Credit Transfers](#TypesofCreditTransfers)
- [File Types Supported](#FileTypesSupported)
- [Cut-Off Time](#CutOffTime)
- [Value Date](#ValueDate)
- [Message Workflow Diagram](#MessageWorkflowDiagram)
- [Outward Processing](#OutwardProcessing)
- [Inward Processing](#InwardProcessing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:33:48 PM IST