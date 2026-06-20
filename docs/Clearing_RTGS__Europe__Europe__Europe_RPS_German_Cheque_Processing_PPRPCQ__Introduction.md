# Introduction to RPS German Cheque Processing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [RPS German Cheque Processing](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
  - [SEPA Credit Transfer SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
  - [SEPA Direct Debit SEPA Direct Debit](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm)
  - [TARGET2 Clearing TARGET2 Clearing](../../Europe/Europe_Target2_PPTGTC/Introduction.htm)
  - [EPC SEPA Credit Transfer EPC SEPA Credit Transfer](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm)
  - [EPC SEPA Direct Debit EPC SEPA Direct Debit](../../Europe/EPC_Direct_Debit/Introduction.htm)
  - [RPS German Cheque Processing RPS German Cheque Processing](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm)
    - [Introduction](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm)
    - [Configuration](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Configuration.htm)
    - [Working with](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Working_with.htm)
    - [Tasks](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Tasks.htm)
    - [Outputs](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Outputs.htm)
  - [VIBER Payments VIBER Payments](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm)
  - [MAV Payments MAV Payments](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm)
  - [Equens SEPA Direct Debit Equens SEPA Direct Debit](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm)
  - [Equens SEPA Credit Transfer Equens SEPA Credit Transfer](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm)
  - [TARGET2 Clearing (ISO20022) TARGET2 Clearing (ISO20022)](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm)
  - [Nordic Credit Transfer Payments Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to RPS German Cheque Processing

Updated On 22 March 2025 |
 27 Min(s) read

Feedback
Summarize

The Retail Payment System (RPS) of Germany offers a cheque processing service to process cheque payments denominated in Euros among German domestic credit institutions. In Germany, the cheques are collected by using either of the following procedures:

[Paperless Cheque Collection Procedure (BSE)](#)

The cheques are exchanged in a paperless format. However, the cheque depository bank can request for paper cheques (if required). This is performed in cheques with value less than EUR 6000.

[Image-Based Cheque Collection Procedure (ISE)](#)

The RPS clearing house receives cheques as electronic images along with the corresponding clearing data record. The corresponding bank forwards the images either to the drawee bank or an institution, which checks the image of the cheque to decide whether it needs to be honoured. The reversal of dishonoured cheques is effected through the clearing house. The relevant cheque images are exchanged through the extranet of Bundesbank. If the corresponding image is unavailable when processing ISE payments, Bundesbank rejects the ISE transaction to the submitting bank. Cheque clearing does not validate the transaction amount for ISE cheques.

## Types of Participants

German Cheque Clearing allows both direct and indirect participants:

| Participant | Description |
| --- | --- |
| Direct | These financial institutions directly clear and settle by using an Exchange Settlement Account, which they maintain with clearing. |
| Indirect | These financial institutions participate in the RPS cheque processing service through a direct participant. Additionally, a direct participant can also submit and receive cheque payments in the RPS cheque processing service for credit institutions with a sub bank license (known as Bank Identifier Code (BIC) holders). |

## Payment Instruments

The German Cheque Clearing System supports only cheque collection.

[Clearing and Settlement](#)

The RPS cheque clearing service performs the Clearing of the payments. The settlement of the successfully processed payments takes place on accounts in the Payments module of the TARGET2 platform.

[Clearing Holidays](#)

The RPS cheque processing service is available on all weekdays, except for the official German national or public holidays and a couple of days in December (24th and 31st).

[Transaction Limits](#)

The following limits are applicable on the transaction amount:

| Cheque Type | Maximum Limit |
| --- | --- |
| BSE Cheques | EUR 5,999.99 |
| ISE Cheques, ISE return Cheques, BSE Return Cheques | No transaction limit |

RPS rejects the individual BSE Cheque transactions amounting to more than EUR 5,999.99.

## Submission Window and Cut-Off Time

RPS cheque clearing performs the clearing and settlement in three windows as follows:

| Window Name | Timings | Type of Request Processed |
| --- | --- | --- |
| Window 1 | 08:00 CET | BSE Cheques, BSE Cheque Returns and ISE Cheque Returns request submitted after 16:00 (D-1) to 08:00 (D) |
| Windows 2 | 10:00 CET | BSE Cheques, BSE Cheque Returns, ISE Cheques and ISE Cheque Returns request submitted after 08:00 (D) to 10:00 (D) |
| Window 3 | 16:00 CET | BSE Cheques, BSE Cheque Returns and ISE Cheque Returns request submitted after 10:00 (D) to 16:00 (D) |

The delivery of the settled cheque collection request or cheque returns from RPS cheque clearing to the direct participants is done after each window. The cut-off time for request processing is defined as follows:

| Cut-Off Time | Cheque Type |
| --- | --- |
| 10:00 CET | ISE Cheque |
| 16:00 CET | BSE Cheques, BSE Cheque Returns and ISE Cheque Returns |

RPS cheque clearing accepts cheque collection request or cheque returns from direct participants any time on business days. If a request is received after the cut-off time, it is processed and submitted to RPS cheque clearing on the next business date with the settlement date set to the next business date.

## Reachability List

The Deutsche Bundesbank publishes a list of the financial institutions that can be reached through the RPS cheque processing service. This list contains the BICs of:

- Direct participants
- Indirect participants
- Available BIC holders

Each BIC represents exclusively oneself; it does not represent a wildcards rule. This list is made available to the direct participants as a CSV file. The directory is published four times a year in its full form. The validity period of the participant directory is the period between its update date and the update date of the subsequent publication. The update date is included in the file name.

## Clearing Rejects

Clearing can reject the cheque collection or cheque returns in case of incorrect submission. The sender of the file receives a DVF (Debit Validation File) from Clearing with the rejection details. Incorrect submissions can result in the following:

- Complete rejection of the received Input Debit File (IDF) file
- Rejection of the cheque collection or return bulks in the IDF file
- Rejection of the individual cheque collection or return transaction

## Re-Submission of Rejected Request

Rejected files (bulk or single payments) can be re-submitted after error correction based on the following aspects:

- Dependencies regarding the respective submission window
- Referencing file (bulk and individual transaction level)
- Assignment of the Interbank Settlement Date (which is data field) within a bulk

## Returns

Banks can reject the received cheque collection request and send back the payment returns.

## Types of Files or Messages

The RPS cheque processing system uses ISO 20022 format file or message types. Submission and delivery of payments is possible only by electronic data transmission. EBICS and SWIFTNet FileAct communication procedures are available for this purpose. The following table lists the different file types that German cheque clearing system supports:

| File Type | Description |
| --- | --- |
| Input Debit File (IDF) | The sending financial institution uses IDF for submission of cheque transactions (pacs.003) or return transaction (pacs.004) in multiple bulks to RPS.  The RPS scheme does not allow the following in the same IDF file:  - Submission of BSE and ISE cheque collection requests - ISE Cheque collection and ISE Returns  Hence, the IDF header has a Service Code Indicator (SIC) to identify the transaction type included in the file. The valid service codes are:  - BSE – Bulks with BSE cheque and/or BSE return cheque transaction - ISE – Bulk ISE cheque transactions - ISR – Bulk ISE return cheque transactions  The following ordering structure is maintained for BSE IDF file, which has both cheque and return transactions:  - File header IDF – pacs.003.002.04SVV (cheque collection) group header (multiple bulks) - Cheque collection transaction information – pacs.004.002.04SVV (cheque return) group header (multiple bulks) - Cheque return transaction information |
| Debit Validation File (DVF) | If there are incorrect submissions, the sender of the file receives a Debit Validation File (DVF) from clearing with the rejection details. Incorrect submissions can result in the following:  - Complete rejection of the received IDF file - Rejection of the cheque collection or return bulks in the IDF file - Rejection of the individual cheque collection or return transaction   If the full file is rejected, only the DVF header is received with the error code set in the IDF Error Code (<IdfErrCd>) element of the DVF header. For bulk and single transaction rejections, pacs.002.002.05SVV is added to the DVF header.  The file structure is as follows:   - File Header DVF – pacs.002.002.05SVV (cheque reject) group header (one bulk) - Cheque reject transaction information and status |
| Result of Settlement File (RSF) | If there is settlement failure at RPS, the sender of the IDF file receives a RSF from RPS.  In case of multiple submitter transactions rejection, it can happen in multiple RSFs with one bulk each depending on their submission. The file structure is as follows:  - File header RSF – pacs.002.002.05SVV (cheque reject) group headers (one bulk) - Cheque reject transaction information and status |
| Unsettled Debit Files (UDF) | If there is settlement failure at RPS, the receiving bank for which the unsettled transactions were intended, receives an Un-Settled Debit File (UDF). In UDF, the details of all unsettled transactions are given for information purposes. Each UDF contains the unsettled transactions of exactly one delivery bucket and grouped together under a group header of the corresponding message type. The file structure is as follows:  - File header UDF – pacs.003.002.04SVV (cheque collection) group header (one bulk) - Cheque collection transaction information - File header UDF – pacs.004.002.04SVV (cheque return) group header (bulk) - Cheque return transaction information |
| Delivery Notification File (DNF) | DNF is used by RPS to deliver the cheque transactions (pacs.003) to the receiving bank. The file structure is as follows:  - File header DNF – pacs.003.002.04SVV (cheque collection) group headers (one bulk) - Cheque collection transaction information |
| Settled Debit File (SDF) | SDF is used by RPS to deliver the return transactions (pacs.004) to the receiving bank. The file structure is as follows:  - File header SDF – pacs.004.002.04SVV (cheque returns) group headers (one bulk) - Cheque return transaction information |

The following table lists the supported business transactions and ISO message types that process these transactions:

| Message Type | Business Transaction |
| --- | --- |
| pacs.003.002.04SVV | Cheque collection message |
| pacs.004.002 .04SVV | Return of a cheque payment |
| pacs.002.002.05SVV | Reject (refunds from the cheque processing service for the defective file, bulk or single payments) |

There is no limit on the number of physical files that can be submitted to RPS in a business day. A physical file can carry up to 999 logical files (bulks). A bulk contains a maximum of 100,000 transaction information details of similar business cases. A physical file received from RPS, contains a single bulk.

## End-Of-Day Reports

At the end of each business day, every participant receives a daily reconciliation report (DRD) at 22:00 CET. These reports contain the total count or value of cheque collections or returns submitted, which are received in the cheque processing service. The DRD is provided in EBCDIC flat file format with the following layout:

- DRD header
- DRD (pacs.003) cheque collection bulks sent body
- DRD (pacs.004) return bulks sent body
- DRD (pacs.003) cheque collection bulks received body
- DRD (pacs.004) return bulks received body
- DRD trailer

The above details are provided separately for BSE, ISE and ISR.

## RPS Cheque Processing

The below workflow depicts the RPS cheque processing message flow.



1. Cheque collection request initiation can happen through the following sources:
   - Bank user using the `Teller` application to initiate payment request
2. TPH module at the sending bank (cheque collecting bank) processes the cheque collection request and sends out the IDF File to RPS at scheduled intervals.
3. RPS cheque clearing validates the file. Debit Validation File (pacs.002SVV) is generated for the following validation failures:

   | Rejection Type | Description |
   | --- | --- |
   | File level rejection of the full IDF file | This results in the RPS clearing sending back a DVF file, with only the header. The reason code for rejection and original file reference is indicated in the header |
   | Bulk level rejection of specific bulks in the IDF file | This results in the RPS clearing sending back a DVF message, against every bulk that is rejected. The Group Status tag contains the RJCT value. The pacs.002 message also carries the reason code for rejection and original bulk message reference. |
   | Rejection of specific transactions in the IDF file | This results in the RPS clearing sending back a DVF file (pacs.002). The Group Status tag contains the PART value with the TxInfAndSts block created for every rejected transaction, specifying the reason code for rejection and original transaction reference. |

TPH module at the sending bank, receives and processes the DVF file. Based on the delivered reject code, the transactions can be sent to an exception queue for further investigation or rejected. In case of rejection, TPH marks the original cheque collection transaction as ‘Rejected’ and performs reversal posting to the creditor’s account.

4. After successful validation, RPS performs the settlement of the cheque collection or cheque return request. If the settlement fails, a result of settlement file (pacs.002 SVV) is generated and sent to the sending bank. The RSF file contains the details of all the cheque collection or cheque return transactions that failed settlement.

Handling of RSF file is out-of-scope of this enhancement.

5. In case of settlement failure, RPS Clearing also generates an Unsettled Debit File (pacs.002 SVV) and sends the same to the receiving bank (drawee bank). The UDF file contains the details of all the cheque collection or cheque return transactions that failed settlement.

Handling of UDF file is out-of-scope of this enhancement.

6. On successful settlement, the cheque collection request is forwarded to the receiving bank (drawee bank) as Debit Notification File (pacs.003SVV). The TPH module at the receiving bank validates and accepts the request and debits the debtor’s account for the requested collection amount. No payment confirmation message is sent to Clearing on successful processing of a cheque collection request.
7. If an inward cheque collection request fails processing at the sending bank, then TPH generates and sends the returns to the clearing as a bulk IDF file.
8. RPS cheque clearing validates the return IDF file.
9. After successful validation, RPS performs the settlement of the cheque return request. In case of settlement failure, the RSF file is generated and sent to the drawee bank.
10. UDF file is sent to the cheque collecting bank for cheque returns that failed settlement.
11. On successful settlement, the cheque return request is forwarded to the cheque collecting bank as Settled Debit file (pacs.004SVV). The TPH module at the cheque collecting bank validates accepts the request, and debits the creditor’s account for the returned amount. The original cheque collection request is marked as ‘Returned’.
12. At the end of every business day, the RPS cheque processing service sends a Daily Reconciliation Report (DRD) file to all direct participants. The file includes the information about the number and value of cheque collection or cheque returns processed for the business day.

Handling RSF file is out-of-scope of this enhancement.

## Outward Processing

This section deals with the outward processing of the cheque collection requests and payment return request in TPH.

[Cheque Collection Request](#)

This below workflow depicts the outward processing of a cheque collection request initiated in TPH.



The following table explains the activities in the workflow:

| Activity | Description |
| --- | --- |
| Payment initiated through teller | Captures a cheque collection request (manually) by using the `TELLER` application.  Validates the mandatory fields and indicates an error (if any).  The creditor account is validated to ensure that it is a valid Temenos Transact account and does not have any posting restriction. |
| Reachability check | Checks whether the financial institutions involved in the transaction can be reached through the RPS cheque processing service. If cheque collection is initiated from `TELLER` application, then reachability is performed by the same. |
| Routing | Routes payments to RPS cheque clearing based on the routing rule maintained in TPH.  Performs the reachability check on the drawee bank BIC (if configured). |
| Clearing – cut-off time validation | Validates whether the cheque clearing cut-off is crossed or not. If the cut-off is past, it moves the settlement date to the next business date.  If a cheque collection request is initiated from Teller, the settlement date is not be updated when the cut-off is crossed. |
| Cheque clearing channel validations | Performs RPS cheque clearing specific validations on the cheque collection transaction to ensure that the transaction meets the requirements of the RPS clearing. XSD validation is also done on the generated outgoing file. |
| Value date calculation | Calculates credit value and exposure dates as follows:     The `Teller` application performs the date calculation for cheque collection request initiated from Teller: |
| Duplicate check | Performs the checks on outgoing cheque collection transactions for the set of payment attributes, such as payment amount, currency, and transaction reference (if required). |
| Filtering | Filters the payments when interfaced to a screening engine. This is a bank specific requirement and to be undertaken at site. |
| Fees calculation | Charges processing fees to a creditor based on the fee products configured in TPH.  For cheque collection transaction created from teller, charges are calculated based on the fee configuration setup in the Teller module. It is also possible to waive off the fees from the `TELLER` application while capturing the cheque collection request. |
| Posting | Configures German cheque collection transactions as pre-settled in TPH. The creditor’s account is credited with the transaction amount with a future exposure date. Charges are debited from the creditor account (if any).  The following postings are done for a cheque collection request:  - Debit clearing suspense account - Credit creditor account (with future exposure date)  The Teller module perform the above posting (except the settlement entry) for Teller initiated cheque collection request. A separate settlement transaction is created and posted for moving funds between the clearing Nostro account and clearing suspense account, after the IDF file is generated. The following postings are performed:  - Debit cheque clearing Nostro account - Credit clearing suspense account  Auto-posting of settlement entries is supported only with a Temenos Payments Hub (TPH) license. |
| Update cheque collection module | Updates the cheque status in the cheque collection module to set the cheque status as ‘Deposited’. |
| Generate and send pacs.003 to clearing | Generates an IDF file by bulking all cheque collection requests. The file submission to the clearing happens at pre-defined clearing schedule. TPH performs XSD validation of the generated pacs.003 IDF file. In case of validation failure, the file is moved to the error queue and no further processing is possible in TPH. |
| Error queue | If an error occurs during validation, it routes cheque collection transaction to the Repair queue for manual intervention. TPH performs routing and clearing file generation only for cheque collection requests initiated from Teller. Other components are skipped through configuration. |

[Payment Return](#)

This section describes the processing of an outward payment return request for a rejected inward cheque clearing request in TPH.



The following table explains the activities in the workflow:

| Activity | Description |
| --- | --- |
| Return initiation | Initiates outward return after the rejection of an inward cheque clearing request that failed processing. |
| Routing | Routes return payment to the RPS cheque clearing channel, as per the routing rule setup in TPH. |
| Clearing cut-off time check | Validates whether the cheque clearing cut-off is crossed or not. If the cut-off is past, it moves the settlement date to the next business date and warehouses the payment. |
| Charge calculation | Collects fees from the customer for unsuccessful processing of cheque clearing transactions. It calculates the fees based on the fee products configured in TPH. |
| Posting | Posts the following entries against the original cheque clearing transaction:  - Debit returns suspense account - Credit cheque clearing suspense account  Posts the following entries against the return transaction:  - Debit cheque clearing suspense account - Credit return suspense account |
| Update the original payment transaction status as returned | Marks the original cheque clearing transaction as ‘Returned’ and update the cheque status in Temenos Transact cheque register as ‘Returned’. |
| Generate return message | Generates an IDF message and forwards it to RPS clearing by bulking all the processed return transaction. The IDF file is sent to the clearing at the pre-defined clearing schedule (clearing frequency configuration). The return transaction status are marked as ‘Completed’. TPH performs XSD validation of the generated pacs.004 IDF file. In case of validation failure, file is moved to the error queue and no further processing is possible in TPH. |
| Repair | Routes return transactions that have validation errors to the repair queue for manual intervention. |

## Inward Processing

This section deals with the inward processing of an incoming cheque clearing request file (DNF), Clearing Reject file (DVF), and Return message file (SDF) from RPS cheque clearing.

[Cheque Clearing Request from Clearing](#)

This section describes the processing of an incoming cheque clearing request file (DNF) from RPS cheque clearing.



The following table explains the activities in the workflow:

| Activity | Description |
| --- | --- |
| Message acceptance | Validates the received DNF file against the schema definition (XSD) provided by the clearing. Schema validation failure results in the rejection of the full file. No return message is created for such rejection. |
| Message mapping | Unbulks the DNF file, maps the file and creates the cheque clearing transaction. |
| Debit account validation | Validates if the debit account is a valid Temenos Transact account, active and does not have posting restriction. |
| Manual verification | Processes cheque clearing transaction either as automated (STP) or manual (non-STP). In case of non-STP, payment is parked to repair queue for manual action by the operator (image and/or signature verification and other manual processes). After manual verification, the user can release the payment for STP processing. If the user does take any action, all payments are released (scheduled release) based on the configured cut-off time. |
| Cheque number validation | Validates cheque details against cheque register in Demand Deposit Account (DDA) or Temenos Transact.  Only when the cheque status is ‘Issued’, the payment is processed further. If the status is already ‘Returned’, a warning is generated for overriding it and going ahead with the represented cheque. |
| Balance check | Checks for sufficient funds in the debtor’s account before posting an inward direct debit. If funds are available, it performs fund reservation. |
| Dates calculation | Sends RPS cheque clearing payments always with the current business date (same day payments). The debit value date is calculated by TPH as the current business date. |
| Duplicate check | Performs duplicate check on cheque clearing transactions based on the following attributes:  - Transaction ID - Creditor Agent ID - Interbank Settlement Date  The fields used for duplicate check can be configured based on the customer requirement. |
| Filtering | Filters payments when interfaced to a screening engine. This is bank specific requirement and is performed in the site. |
| Charge calculation | Charges customer fees based on the configured fee product. The calculated fee is applied on the customer’s account during posting. |
| Debit posting | Debits the debtor’s account with the transaction amount. The following postings are done for a cheque clearing request:  - Debit debtor’s account - Credit cheque clearing suspense account  A separate clearing settlement transaction is created and posted for moving funds between the cheque clearing Nostro and clearing suspense account when the DNF file is processed. The following postings are done for the same:  - Debit cheque clearing suspense account - Credit cheque clearing Nostro account  Auto-posting of the settlement entries is supported only with a TPH license |
| Update cheque status | Updates the cheque status in Temenos Transact cheque register as ‘Cleared’. |
| Repair | Routes inward cheque clearing transactions that have validation errors to the repair queue for manual intervention or rejects automatically (based on configuration). For transactions routed to repair, the user can repair the transaction from the repair screen or manually return the transaction with a specific return reason code. Automatic return processing is available only with a TPH license. |

[Reject File](#)

This section describes the processing of a Clearing Reject file (DVF) received from RPS cheque clearing.



The following table explains the activities in the workflow:

| Activity | Description |
| --- | --- |
| Message acceptance | Validates the received DVF file as per the schema definition provided by the clearing. |
| Check DVF type | Determines the type of rejection received in DVF and performs either of the following process:  - Full File reject – TPH only updates the status of the original IDF file as ‘Rejected’. Any further handling to resubmit the file or reverse the original credit postings has to be done outside TPH. - Bulk or Transaction level reject – In case of DVF file received for bulk or transaction level rejection, it is possible to send the payments to exception queue for manual handling based on the reject reason code received in the DVF file.  Users can resubmit the original payment from the exception queue or reject the original payment. |
| Update cheque status | Sends the rejection details to the Cheque collection Module for updating the cheque status as ‘Returned’. The cheque collection module posts the required reversal accounting entries.  - Debit customer account - Credit cheque clearing suspense account |
| Update original payment as Rejected | Marks the original Cheque Collection transaction as ‘Rejected’. |
| Posting | Posts the following settlement entries:  - Debit cheque clearing suspense account - Credit cheque clearing Nostro account  Auto-posting of settlement entries is supported only with a TPH license. |

[Return Message](#)

This section describes the processing of a Return message file (SDF) received from RPS cheque clearing.



The following table explains the activities in the above workflow:

| Activity | Description |
| --- | --- |
| Message acceptance | Validates the received SDF file as per the schema definition provided by the clearing. Schema validation failure results in the rejection of the full file. |
| Update cheque status | Sends the return details to the cheque collection module, to update the cheque status as ‘Returned’. The cheque collection module performs the required reversal postings.  - Debit customer account - Credit cheque clearing suspense account |
| Update original Payment as Returned | Marks the original cheque collection transaction as ‘Returned’. |
| Posting | Posts the following settlement entries after the return file is processed:  - Debit cheque clearing suspense account - Credit cheque clearing Nostro account  Reversal postings are based on the original cheque collection amount  Auto-posting of settlement entries is supported only with a TPH license. |
| Auto-Clear | Updates the status of cheques (automatically) to ‘Cleared’when returns are not received till the credit value date. This can be enabled through standard configuration. |

## Illustrating Model Parameters

Read the [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Suite (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) user guides for information on parameter setup for Cheques and Cheque Returns.

## Illustrating Model Products

This module provides facility to initiate and receive Cheque requests through RPSCHQ Clearing.

In this topic

- [Introduction to RPS German Cheque Processing](#IntroductiontoRPSGermanChequeProcessing)

- [Types of Participants](#TypesofParticipants)
- [Payment Instruments](#PaymentInstruments)
- [Submission Window and Cut-Off Time](#SubmissionWindowandCutOffTime)
- [Reachability List](#ReachabilityList)
- [Clearing Rejects](#ClearingRejects)
- [Re-Submission of Rejected Request](#ReSubmissionofRejectedRequest)
- [Returns](#Returns)
- [Types of Files or Messages](#TypesofFilesorMessages)
- [End-Of-Day Reports](#EndOfDayReports)
- [RPS Cheque Processing](#RPSChequeProcessing)
- [Outward Processing](#OutwardProcessing)
- [Inward Processing](#InwardProcessing)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [APIs](../../APIs/Misc/APIs.htm#EP)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:09 PM IST