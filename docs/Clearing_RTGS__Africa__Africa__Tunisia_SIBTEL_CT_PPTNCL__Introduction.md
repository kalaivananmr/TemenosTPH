# Introduction to Tunisia Credit Transfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm) > Introduction

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
    - [Introduction](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
    - [Configuration](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Configuration.htm)
    - [Working with](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Working_with.htm)
    - [Tasks](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Tasks.htm)
    - [Outputs](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Outputs.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Introduction to Tunisia Credit Transfer

Updated On 23 May 2023 |
 14 Min(s) read

Feedback
Summarize

Tunisia clearing supports incoming, outgoing and return of Credit Transfer (CT), and incoming clearing reports, based on the rules defined by Clearing House in Tunisia (SIBTEL). SIBTEL is a net settlement system designed for settlement of payments in Tunisian Dinar (TND) currency with a maximum transaction limit of 10000 TND. It uses flat files to send and receive payment messages.

## Types of Messages

Tunisia clearing uses the following flat files to send or receive payments messages:

| File | Description |
| --- | --- |
| Outbound CT | Participants of Tunisia bank sends the file to the SIBTEL clearing system. |
| Inbound Return | SIBTEL clearing sends the file to debtor bank on behalf of the creditor bank for automatic processing of returned CT. |
| Inbound CT | SIBTEL clearing system sends the file to all the Tunisia bank participants for crediting their customers. |
| Outbound Return | Creditor bank sends the file to SIBTEL for returned transactions, which cannot be credited. |
| CRS | Clearing reports with details regarding the files exchanged with the clearing. |

## Architectural Diagram of SIBTEL CT

The below workflow shows the process of payment between channels and Tunisia clearing by using TPH.



| Item | Description |
| --- | --- |
| Customer Payment Channels | Electronic channels or aggregators of TPH banks (such as mobile and internet banking) |
| Payment Order | Front-end TPH module to manually capture or receive CT instructions from customer channels |
| Payment Engine | Payment system from TPH to process the CT payments |
| SIBTEL System | Transfer payment (clearing) system of Tunisia |
| Transact or External DDA | Core banking system of TPH banks |

## Workflow of Tunisia Clearing File

The below workflow shows the process of transferring clearing files in TPH.



- System collates the CT payments (by Debtor Institution) and at a scheduled time, it generates and sends the transfer files to SIBTEL in the required format.
- SIBTEL collates these files from all the debtor institutions and forwards it to the creditor institution specifying the transfers for their respective customer accounts. The creditor institution validates these payments and credits the customer’s account.
- Creditor institution sends a return file for failed transactions with the clearing defined return codes. This can be sent to SIBTEL till the next working day.
- SIBTEL forwards the return file to the debtor institutions, where it processes and credits the customer’s account with the transfer amount.
- Outgoing transfer file can be sent multiple times to clearing. However, the cut-off time for sending the file is 14:30 (Tunisia time). If a payment breaches the cut-off time, it warehouses the file until the next working day.
- Temenos Payments Hub receives the CRS reports from clearing. An enquiry is used to map and display the data. The user needs to manually handle the data for further processing.

## Types of Participants

Temenos Payments Hub (TPH) supports both direct and indirect participant flows. The source, channel and clearing settings are defined separately based on whether TPH is acting as a direct or indirect participant for Tunisia clearing. To know more, refer to [Configuration](Configuration.htm#top) section.

## Dates

TPH performs channel cut-off and holiday checks (clearing, currency and country holiday) on the Tunisia transfers. Standard business date functionality in TPH applies for SIBTEL payments. However, it warehouses the CT payments generated after cut-off time and can have settlement date as next working date. To know more, refer to [Configuration](Configuration.htm#top) section.

## Routing

TPH routes the payment to other suitable payment channels in that location, when the criteria for Tunisia transfer is not met. System has the ability to route to multiple payment channels based on rules. To know more information, refer to [Routing and Settlement](../../Payments_Hub_(PP)/Routing_and_Settlement/Introduction.htm#top).

TPH sends the payment to Repair queue, when:

- Transaction amount is more than 100000 TND
- System misses the cut-off and fails to route the payment

## Charges

Charge type is mapped to SHA for Tunisia transfers and the system applies the standard charge calculation logic in TPH.

## Clearing Directory and Reachability

TPH supports loading of the SIBTEL clearing directory and reachability check. The directory receives upload at irregular intervals from SIBTEL. The reachability check for Tunisia transfers is performed using clearing specific reachability API, based on bank code (sort code) of the receiving bank and channel. To know more, refer to [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm#top).

## Cut-Off Time

When TPH processes all CT payments, a CT file is sent to the clearing. Clearing forwards this file to the creditor bank to credit their accounts with credit transfer payments. This CT file is sent to clearing before 14:30 Tunisia time (configurable).

## Manual Entry of Tunisia Transfer

TPH supports manual capture of CT payment from branch or back-office by using Payment Order page to send Tunisia transfers to SIBTEL. This page is exposed as a Restful API to the bank’s channels (such as internet and mobile banking), if required. User can enter the debtor account along with payment amount, currency and beneficiary ID. The beneficiary ID has the details of the beneficiary RIB (Format of the account number in Africa, which is similar to IBAN) and sort code of the credit bank. To know more, refer to [Working with](Working_with.htm#top) section.

## Outward Processing

This section describes the process of outward payment transfer and return file.

[Outward Payment](#)

TPH validates, collates and sends the Tunisia CT payments to SIBTEL clearing in the required format before the cut-off time. Clearing forwards this to respective creditor institution, which validates and credits the respective customer’s account.



| Activity | Description |
| --- | --- |
| Manual capture of credit transfer payment from branch or back-office using PO application page | Captures a CT payment from PO application page for Tunisia Transfers. User enters the debtor account with payment amount, currency and beneficiary ID. The Beneficiary ID has the details of the Beneficiary RIB and sort code of credit bank. |
| Account validations | Validates whether the debit account is valid, has sufficient balance for CT payment, and no posting restrictions |
| Clearing level validations | Validates the following, as part of the clearing validation API for outgoing payments:  - Currency is TND - Account number is not null for the credit party roles (beneficiary and account with institution) - OrginatorResidency, OrginatorAcctNature or OrginatorAcctType is not left blank - Last two check digits of the RIB (Account Number format in Africa) or 20 digit Tunisia account number is replaced by 00, and their Modulo 97 is derived as shown below to arrive at the check digits. For example, if the account number is 14005005101700376458, the cheque digits are = 97- ((14005005101700376400) Modulo 97)  = 97-39  = 58 |
| Balance reservation | Reserves the balance in the debit account for the CT amount |
| Routing, reachability and channel cut-off | Determines the routing channel based on the product setup of CT payment and performs channel validation (such as reachability) based on the bank code and cut-off time check |
| Filtering | Filters the payment when interfaced to a screening engine. This is a bank specific requirement and is performed in the site |
| Debit posting | Debits the customer account and credits the clearing suspense account, when the validations are successful |
| Generation of the CT file | Collates all CT payments in 706 status (to be sent to SIBTEL) and forms a CT file (flat file) in the clearing specification (which is sent to the clearing based on the clearing frequency defined in the system). TPH generates a unique seven-digit reference number to send it in the outgoing file for Tunisia transfers. |
| Error or repair queue | If an error occurs during processing, it moves the transaction to Repair queue for user to repair, resubmit or cancel the payment (with a description). During repair and resubmission, the process flow is re-executed from account validation. The cancelled payment moves to ‘Cancelled’ status. |

[Outward Return File](#)

This section describes the process of return request in TPH for an inward CT. If credit institution (TPH bank) cannot process the payment received (due to an error), TPH generates the return file with a reason for return and forwards it to clearing. This is forwarded to the debtor institution, where the system processes the returns and credits the customer’s account with transfer amount.



TPH can return a previously settled incoming CT within the prescribed number of days following the interbank settlement date. The bank can initiate a return for one of the following reasons:

- Objection for other reasons
- Deceased account holder
- Closed account
- Incorrect information
- Funds origin not justified
- Misdirected value
- Other reasons

The application initiates the return within allowed number of days (from the original transaction inter-bank settlement date) and sends it as an ‘Outbound Return File’ to clearing. On processing the return, TPH updates the return transaction status as ‘Completed’.

| Activity | Description |
| --- | --- |
| Return initiation | Initiates an outward return, after an inward CT payment fails processing |
| Routing | Routes the return payment to SIBTEL, according to the routing configuration setup in TPH |
| SIBTEL cut-off time check | Verifies whether SIBTEL cut-off time is not crossed. If crossed, it warehouses and sends the return on next business date in automated returns (with PH license). In manual returns, it triggers an error for cut-off or return acceptance day breach (if configured). |
| Posting | Posts the following entries for original CT transaction:  - Debit clearing suspense account - Credit returns suspense account  Posts the following entries for new return transaction:  - Debit returns suspense account - Credit clearing suspense account |
| Generate return file and mark the original payments as ‘Returned’. | Marks the following statuses:  - Original return transaction as ‘Completed with Return’. - Return transaction as ‘Complete’, when it is sent to clearing as a return file. |
| Repair | Displays routing errors (such as cut-off or return acceptance day breach) in the Repair page (if configured) for returns. |

## Inward Processing

This section describes the process of inward payment transfer and return file.

[Inward Payment](#)

TPH processes incoming Tunisia CT payments received from SIBTEL clearing. It validates the message during processing before crediting the respective customer account.



| Activity | Description |
| --- | --- |
| Inward transfer from SIBTEL network | Accepts and maps the inward CT payment received from SIBTEL |
| SIBTEL specific format validations | Performs SIBTEL specific validations on payments |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary account number is invalid - Beneficiary account is closed - Posting restrictions |
| Dates calculation | Determines the value date as current business date and processes the payment immediately |
| Filtering | Filters the payments (if configured). This is a bank specific requirement and is performed in the site.  TPH is interfaced to Financial Crime Mitigation (FCM) module of Temenos. |
| Fee calculation | Calculates the charges associated with the payment and debits it from the customer account |
| Duplicate check | Performs the check on payment amount, currency and transaction reference received from SIBTEL |
| Credit posting | Raises the following accounting entries for an incoming CT **Settlement Entry (Bulk)**   - Debit clearing nostro - Credit suspense account   **Child Transaction**   - Debit suspense account - Credit customer account |
| Error queue | If an error occurs during CT payment processing, it moves the transaction to Error queue for user to repair or manually return the payment. |

[Inward Return File](#)

When the beneficiary bank is unable to credit the beneficiary account, it can return the payment. Clearing receives an inward file for returns. These return files are processed as an inward return of a CT in TPH.



| Activity | Description |
| --- | --- |
| Return file received in TPH | Receives and accepts the return file |
| Return processing | Checks for the following:  - Original CT payment based on original unique reference, amount, and value date - Receives return within the allowed days, if configured in the system for SIBTEL |
| Credit account validations | Validates the credit account in core banking system for posting restriction, closure and other validations |
| Posting | After validating the original transaction, TPH passes the accounting entry to perform the following and marks it as ‘Completed with Return’:  - Debit the return suspense - Credit the customer’s account for the CT payment return  If the original is not found, it moves the payment to Repair queue for manual intervention. |

## CRS Reports Received from Clearing

CRS files (CRS-21 and CRS-22) are clearing reports which has the total number of transactions exchanged or rejected between the clearing and bank. The type of CRS files received for Tunisia transfers are as follows:

- CT presentation record details
- CT rejection record details

The EB.FILE.UPLOAD application is used to upload all the CRS files (in TPH) received from the clearing. The records are stored in PP.CLR.REPORTS.FILE table. Operator can query the CRS report stored in TPH. To know more, refer to [Working with](Working_with.htm#top) section.

In this topic

- [Introduction to Tunisia Credit Transfer](#IntroductiontoTunisiaCreditTransfer)

- [Types of Messages](#TypesofMessages)
- [Architectural Diagram of SIBTEL CT](#ArchitecturalDiagramofSIBTELCT)
- [Workflow of Tunisia Clearing File](#WorkflowofTunisiaClearingFile)
- [Types of Participants](#TypesofParticipants)
- [Dates](#Dates)
- [Routing](#Routing)
- [Charges](#Charges)
- [Clearing Directory and Reachability](#ClearingDirectoryandReachability)
- [Cut-Off Time](#CutOffTime)
- [Manual Entry of Tunisia Transfer](#ManualEntryofTunisiaTransfer)
- [Outward Processing](#OutwardProcessing)
- [Inward Processing](#InwardProcessing)
- [CRS Reports Received from Clearing](#CRSReportsReceivedfromClearing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:34:03 PM IST