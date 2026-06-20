# Introduction to InterGIRO2 (IG2) Credit Transfer (CT)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
    - [Introduction](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
    - [Configuration](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Configuration.htm)
    - [Working with](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Working_with.htm)
    - [Tasks](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Tasks.htm)
    - [Outputs](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Outputs.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
  - [SEPA Credit Transfer SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
  - [SEPA Direct Debit SEPA Direct Debit](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm)
  - [TARGET2 Clearing TARGET2 Clearing](../../Europe/Europe_Target2_PPTGTC/Introduction.htm)
  - [EPC SEPA Credit Transfer EPC SEPA Credit Transfer](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm)
  - [EPC SEPA Direct Debit EPC SEPA Direct Debit](../../Europe/EPC_Direct_Debit/Introduction.htm)
  - [RPS German Cheque Processing RPS German Cheque Processing](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm)
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

# Introduction to InterGIRO2 (IG2) Credit Transfer (CT)

Updated On 22 March 2025 |
 38 Min(s) read

Feedback
Summarize

IG2 is a local interbank clearing system of Hungary that processes only credit transfers. It accepts payment instructions from participants (throughout the day) in multiple clearing cycles from Monday to Friday.

Saturdays can be declared as working days on adhoc basis with limited cycles.

IG2 performs the following:

- Validates the payment
- Updates settlement obligations
- Attempts to settle the obligations in Hungary RTGS (on successful settlement, it routes the payment to the destination bank)

The beneficiary bank makes the credit available to the beneficiary on the same day the payment is received from IG2. IG2 clearing scheme is aligned to SEPA standards, which allows Hungarian domestic Credit Transfer (HCT) to be associated to SEPA Credit Transfer (SCT) (but tailored for local use). Bank-to-Bank settlement happens in 10 settlement sessions (that is, every hour) for a day. IG2 settles in net settlement mode in Hungary’s RTGS is known as VIBER. The workflow of IG2 Hungarian CT Overall message is as follows:



The following are the messages types in IG2:

| Message Type | Description |
| --- | --- |
| pacs.008 (Input Credit File) | In an onward forwarded post settlement:  - Originating participant bank sends CT to IG2 - Beneficiary bank receives CT from IG2 clearing |
| pacs.002.V | IG2 sends the process validation payment status report as a response to outward credit transfer request. |
| pacs.004 (Input Credit File) | Beneficiary bank returns the payment:  - In the event of an issue with the credit account  - As a positive answer to a recall request |
| camt.056 (Input Credit File) | Originating bank initiates a cancellation request to cancel an outward credit transfer |
| pacs.002.C | IG2 deletes the credit transfer request for the following, when it sends cancellation payment status report to originating bank:  - Settlement failure - Cannot be rolled over - Successful recall from originating bank |
| camt.029 | Generates or receives negative answer to an inward cancellation request or outgoing cancellation request, respectively |

## Types of Participants

The two type of participants in IG2 HCT payments are as follows:

| Type of Participant | Description |
| --- | --- |
| Direct | A member bank that exchanges payments directly with IG2 and holds a settlement account in VIBER (Hungary RTGS). |
| Indirect | A member bank that exchanges payments indirectly with IG2 through a direct participant. Indirect participant does not hold a settlement account in VIBER (Hungary RTGS) but settles in the account of its direct participant. Currently, IG2 in TPH does not support Indirect Participant. |

## Types of Payment and Messages

TPH supports the following IG2 HCT message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.02 | B2B | **Payment Request**  Payer bank sends the request to IG2  - IG2 receives the request from the payee bank   TPH supports the EPC version (pacs.008.001.02). | Inward and outward |
| pacs.002.001.03 | B2B | **Payment Response**  This is also known as Payment Status Report (PSR) or Cancellation Payment Status Report (CPSR). Payer bank receives the request from IG2 in response to pacs.008 or camt.056. TPH supports the EPC version (pacs.002.001.03). | Inward |
| pacs.004.001.02 | B2B | **Payment Return**  The Payee bank performs the following: Sends the request to IG2 to return an inward payment.  - Receives the request from IG2 to return an earlier sent outgoing payment - Sends a request to IG2 as a positive response to an inward cancellation request (camt.056)   TPH supports the EPC version (pacs.004.001.02). | Inward and outward |
| camt.056.001.02 | B2B | **Payment Cancellation Request**  The payer bank performs the following:  - Sends the request to IG2 for an outward payment request to be cancelled. - Receives the request from IG2 for an inward payment request to be cancelled.   TPH supports the EPC version (camt.056.001.02). | Inward and outward |
| camt.029.001.03 | B2B | Negative Response to an Inward Cancellation Request Payee bank sends the request to IG2 as a negative response to an inward cancellation request (camt.056). TPH supports the EPC version (camt.029.001.03). | Inward and outward |

## Payment Instruments

IG2 HCT is an IG2 payment instrument.

## Bank and Account Identifier

Banks in Hungary are uniquely identified by either GIRO Routing Code also known as G-Code (length 8) or BIC (length 11). Accounts are identified by using the following:

- BBAN is a 24 digit structure that comprises of bank code (3 digits), branch code (4 digits) and account number (16 digits).
- IBAN is combination of BBAN and country code with CDV, and has total length of 24 characters.

IG2 accepts account numbers in IBAN format only.

## Clearing Directory and Reachability

TPH fully supports GVT clearing directory and uploads the full GVT file (automatically) when the bank receives it regularly on monthly or adhoc release from GIRO. Effective date of the GVT file (in the file name) is a future date.

- If a GVT file with current or past date is uploaded, TPH uploads the records with effective date as the next calendar date.
- If a new set becomes effective (on the designated effective date), the previous set becomes obsolete and is not referred by TPH. The obsolete set is purged by an automated Temenos Transact purge process on a designated date according to the configuration.

The bank users can view and amend the loaded GVT records in TPH.

Reachability is performed based on G-Code of the beneficiary bank. The G-Code is derived from the creditor account number (IBAN or BBAN). On validation, if the G-Code is an indirect participant (G-Type is I), BIC of the direct participant is retrieved by using Routing Code in *G-Direct* field. Reachability is configured to be validated from PAYMENT.ORDER (PO) application (during manual payment capture) and TPH (during STP processing). It performs the following:

- Validates only outward payments for reachability
- Does not validate the outward recall requests, returns and recall response, and inward payments

- It parks the payments that failed reachability check in the Repair queue.
- To know more, refer to [Directory Upload](../../Clearing_Directory_(CA)/Misc/Introduction.htm#Clearing_Directory_Upload).

## Warehouse

The following are the warehouse payments:

| Payment Type | Description |
| --- | --- |
| Outward | **Future Dated Payments instructions**  - IG2 does not accept future dated payments. - TPH warehouses the future dated payment instructions received from customer (to be cleared by using IG2) until the execution date instructed in the payment instruction.   It releases future dated payments on the execution date at 6 AM. **Same Day Payments instructions**  - IG2 accepts same day payments only. - Any payment instructions received from the customer with execution date same as the current business date in TPH are processed STP.   - If same day payment instructions are received before 6:00 AM, they are warehoused until 6:00 AM. - If same day payment instructions are received after the clearing cut-off time, they are warehoused and processed on the next working day in the first clearing cycle(if configured). |
| Inward | Payments received from IG2 are always for the same business day (same day payments). There is no warehousing configured in TPH for inward payments. |
| Timed Release Warehouse | Payments received with same day processing but before ‘Release Warehouse Time’ are warehoused in TPH. Payments subjected to timed warehouse release are timestamped with the proposed release warehouse time.  - Future dated payments – It performs the timestamping on the SOD of the execution date. - Same date payments – It performs the timestamping once it is received and processed.  Timed Warehouse functionality is applicable for all payments instructions initiated from Temenos Transact applications (for example, STANDING.ORDER and PO applications) and payments from electronic channels through single or batch payments (such as received in pain.001). Bulk payment initiation instructions (pain.001) are received in TPH with indication to perform one of the following:  - Single debit multiple credit booking - Multiple debit multiple credit booking  Earlier, timed warehouse is performed on batch leg (that results in warehousing the batch leg and its related credit transactions). Currently, timed warehouse is performed directly on the individual transactions (as there is no batch leg). The Recall, Return and Payment status reports are not subjected to timed warehousing. A Temenos Transact warehouse release job is configured to run at 6 AM, hence, IG2 payments in warehouse are released for processing. |

## Clearing Validations

IG2 clearing specific validations are included in the API to validate all outgoing IG2 files. The validations are as follows:

- Currency needs to be HUF
- Local instrument proprietary needs to be either 001-00 (single credit transfer) or 007-01 (multiple credit transfer)
- Name of CSM needs to be IG2
- Valid end-to-end reference needs to be available
- Return file needs to be sent within five clearing days

[Homogenous File](#)

TPH generates HCT bulk payment files to IG2 (as UNIFI XML files with one or more standard SEPA XML transactions) at pre-defined frequencies according to the pre-defined naming convention. One file cannot have credit transfer, return or cancellation items at the same time.

## Credit Transfers

IG2 processes the payments in designated clearing sessions for outgoing credit payment request as follows:



1. Bank user can capture the payment (manually) in the PO application as single payments and send the pain.001 bulk directly to TPH.
2. TPH processes and sends the payment to IG2. It generates the Bulk Credit Transfer Payment files (pacs.008) at pre-defined frequency and forwards it to IG2 clearing.
3. IG2 validates the payment file and accepts (fully or partially) the credit transfer request or rejects the file.
   - If the validation fails and is sent to the payer bank as a response, it generates the validation payment status report (pacs.002.V).
   - If the validation is successful at IG2, it attempts to settle the payments.
   - If the payment cannot be settled, it generates and sends the cancellation payment status report (pacs.002.C) to the payer bank.
4. On successful settlement, it forwards the payment to the payee bank (pacs.008).
5. On receipt of the credit transfer, the payee bank performs the below actions:
   - Validates and accepts the request, and credits the beneficiary. No payment confirmation message is sent to clearing or originating bank for an inward credit transfer request.
   - If the payee bank is unable to credit the beneficiary, then return is sent to IG2.

## Return a Payment

TPH (as a Payee bank) generates the bulk payment return files for failed inward credit transfer (pacs.008) as follows:



1. If an inward credit transfer request fails to credit the beneficiary at payee bank, then TPH generates the returns and sends it as a bulk to the clearing (IG2). The return bulk has original message ID (Bulk ID) of the settled batch.

IG2 checks for the following:

- All the fields in the Return Credit Transfer (RCT) are matching with the corresponding fields in the Original CT (that is, ‘exact copy’)
- Return is received within the SLA (5 days).

2. IG2 performs the following:
   - If the pacs.004 validation fails, it rejects the pacs.004 transaction by sending NAK pacs.002. TPH updates the payment status accordingly.
   - If pacs.004 validation is successful, it forwards the pacs.004 to payer bank.
3. On receipt of return request from IG2, the payer bank finds the original payment and marks it as returned.

## Recall a Payment

The following is performed during recall processing:



1. Bank user (as requested by a customer or an IT operations user) initiates the manual recall in PO application.
2. TPH process the request, validates for cancellation acceptance days, and forwards to IG2 as camt.056.
   - If the original credit payment is not forwarded to payee bank, then IG2 sends cancellation payment status report (pacs.002.v) with status as ‘Rejected’ to Payer bank.

     TPH bank reverses the accounting entries and marks the original payment as ‘Rejected'.
   - If the payer bank makes the cancellation request within the permitted time interval and meets exact copy requirement (IG2 matches all fields in recall answer with their corresponding fields in the antecedent CT referred in recall answer), then IG2 forwards the recall request to the payee bank.
3. TPH performs the following actions, when inward cancellation request (camt.056) is received:
   - Validates whether the cancellation request is a valid request and is within the permitted due days.
     - If the request is valid and within permitted due days, the bank user accepts the recall request in TPH (post consent from the debtor) based on the following:

       - If the original payment was fully processed, it reverses accounting and marks the payment as ‘Returned’.
       - If the original payment is not complete (that is, failed and parked in a repair queue), it parks the incoming camt.056 in manual queue as unmatched items.
     - If the recall request is not valid or within permitted due days, it rejects the recall request and sends camt.029.
4. If recall request is accepted at Payee bank, it sends a positive response (pacs.004) to IG2.
5. IG2 validates the pacs.004 (recall response) and performs one of the following:
   - If the pacs.004 validation fails, IG2 sends NAK pacs.002.
   - If the pacs.004 validation is successful, IG2 forwards the request to payer bank. On receipt of return request from IG2, the payer bank finds the original payment and marks the status as ‘Returned’. It creates a new return transaction (pacs.004) and processes to completion.

## Payment Status Report

IG2 sends the payment status report to the payer bank (as a response to credit transfer request file validation) as follows:



1. Payer bank sends credit transfer request to IG2 after debit posting.
2. IG2 clearing validates the credit transfer request (pacs.008).
   - If all transactions are accepted, then it sends payment status report (pacs.002) to payer bank with status as ‘Accepted’. The payer bank marks the transaction as ‘Completed’.
   - If some of the transactions fails, it sends payment status report (pacs.002) to payer bank with status as ‘Partially Accepted’. The payer bank reverses the accounting entries for the rejected payments and marks the transaction as ‘Rejected’.
   - If all transactions fails, it sends payment status report (pacs.002) to payer bank with status as ‘Rejected’. It does not provide debit posting for the rejected payment and marks the transaction as ‘Rejected’ in the payer bank.
   - If any other statuses are received (other than Accepted/Partially accepted /Rejected) from IG2 clearing for the credit transfer, the payer bank retains the status without any action.

Additionally, IG2 sends the cancellation payment status report for the following:

- Receives the recall request is received for credit transfer payment, where pacs.008 is still in pending status at IG2 and not forwarded to Payee bank.
- Unable to process the credit transfer request in the available clearing sessions due to reasons, such as ‘lack of funds’, ‘suspension of either sender or receiver of CT/RCT transactions’, or ‘No clearing processing’.

## IG2 HCT Cut-Off Time

TPH is configured with 10 sending cycles every one hour (that applies for pacs.008, camt.056 and pacs.004). Payment instructions are sent throughout the day (starting from time of warehouse release in the morning hours) until 17:00 hours, which is the cut-off time for the IG2 day. Payments that have breached the cut-off are parked by advancing the execution date.

TPH does not provide any separate configuration for Saturday cycles.

## Bulking Criteria

A file sent to IG2 is an Input Credit File (ICF). The outgoing file can have one bulk with multiple transactions. The outgoing file has only one message type (pacs.008, pacs.004, camt.056, camt.029) bulked in a file. Different message types cannot be bulked in one bulk (that is, pacs.008 and pacs.004 cannot be bulked together in same bulk but can be bulked as two separate bulks in the same file). HCT files are bulked before sending to IG2 clearing based on the following bulking criteria:

- Clearing Currency
- Outgoing Message Type
- Credit Value Date
- Debit Value Date
- Clearing Transaction Type

The Message Format Validation API validates the HCT specific fields for IG2 clearing.

[](#)[Outward File Naming Convention](#)

The outward file name format includes only the BIC, REF, and EXT information and does not include the session ID. The banks generate outward files (pacs.008, pacs.004, camt.056, camt.029) for Inter Giro2 (IG2) without the session ID as part of the file name.

The existing PPHIG2.GENERATE.PHYSICAL.FILENAME API is modified to remove the session ID from the file format.

## Outward Payment Request

Payment can be initiated from Payment Order, Order Entry (OE) or through a pain.001 file (message initiated by customer). The below workflow depicts the processing activities involved in the payment:



| Activity | Description |
| --- | --- |
| Manual capture of IG2 CT payment from branch or back-office by using PO application | Captures an IG2 HCT payment from PO application. Validates mandatory and non-mandatory fields on submission and displays an error (if any). |
| Payment initiation through pain.001 message | Customer can initiate an IG2 credit transfer by sending a pain.001 (EPC standard) message to the ordering bank. |
| Receive and map | Receives, validates and maps the pain.001 message. If the pain.001 message format validation fails, TPH moves it to Error queue. Pain.001 can have one or more customer batches. |
| Debulking | Debulks to single transactions, when the pain.001 is a batch payment (single debit multiple credit). |
| Business validations | Checks for the following:  - Ordering account is a valid Temenos Transact account (or from a bank specific account keeping systems according to the local site specific functionality), which has sufficient balance to cover the transaction and no posting restrictions - IBAN structure of the account of the originator and beneficiary - BIC against BIC directory (if configured) |
| Reachability check | Validates whether the beneficiary bank (GIRO routing number) is reachable directly or indirectly (if configured). To know more, refer to [Clearing Directory and Reachability](#Clearing_Directory_and_Reachability) section. |
| Submission and supervisor approval | Performs the following actions:  - On submission of the payment, it waits for supervisor's approval.   - Once approved, it is moved for further processing.   - If rejected, it modifies and resubmits the payment for approval. The payment is then sent to Temenos Payments Hub Engine for further processing.   Payments received in TPH from external banks in STP mode do not wait for Supervisor’s approval. |
| Warehouse payments | Warehouses the payments with future execution date and same day payments that were received before IG2 warehouse release time (6 AM configurable). All warehoused payments are then released on their execution date at 6 AM by a Temenos Transact scheduled job. To know more, refer to [Warehouse](#Warehouse) section. |
| Balance reservation | Reserves the funds on the debit account, and performs balance reservation on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Duplicate check | Performs duplicate check on payments received from an ordering or indirect participant bank for payment attributes, such as payment amount, currency, and transaction reference. |
| Dates calculation | Calculates the payment value date and booking date, which is configured to current date (same as execution date) |
| Routing | Routes the payment to TPH clearing channel (IG2). Clearing channel determines the message type (pacs.008). |
| IG2 Channel validations | Performs all IG2 specific validations on the payment to ensure it meets the compliance requirements. |
| Cut-off validation | Validates IG2 final cut-off time.  To know more, refer to [IG2 HCT Cut-Off Time](#IG2_HCT_Cut-off_time) section. |
| Fee calculation | Calculates the applicable charges (if configured) |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is bank specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor’s account. If posting fails due to insufficient funds, it parks the payment in Repair queue for user action (reject or cancel) or automatic retry based on configuration.  - If Account Management System (AMS) is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward Payments - Entries made before sending pacs.008 to IG2 HCT The following are the credit transaction entries:  - Debit debtor account (or ordering bank account), single or multiple based on ‘batch booking’ instruction in payment initiation - Credit suspense account - Settlement transaction entries (bulk) - Debit suspense account - Credit IG2 clearing Nostro account |
| Bulking | Bulks the transactions to batches according to bulking configuration. A single bulk can have 10,000 transactions. To know more, refer to [Bulking](#Bulking_Criteria) section. |
| Outward payment generation | Generates pacs.008 at the end of every clearing session |
| Error queue | If the pain.001 batch fails due to message format validations, it parks the payment in the Error queue. |
| Repair queue | If an outward pacs.008 payment generation fails in any component in TPH STP flow, it moves the transaction to Repair queue for the user to repair or cancel the payment. The repaired payments continue with payment processing starting from debit account validations. |

## Inward Payment Request (pacs.008)



| Activity | Description |
| --- | --- |
| IG2 HCT payment received from IG2 clearing | Receives an inward payment pacs.008 from IG2 |
| HCT specific format validations | Performs schema validation on the payment  - If the validation fails, it moves the message to the Error queue |
| Account validation | Performs the following business validations:  - Beneficiary account invalid - Beneficiary account restrictions - Beneficiary account type does not allow to credit external transfer items (product configuration) - Beneficiary account is closed - Beneficiary account is blocked with a specific code (for example, criminal block) |
| Dates calculation | Sends IG2 payments with current business date (same day payments).   - Calculates the value date based on the current business date. |
| Fee calculation | Calculates the fee and collects it in TPH based on the configuration |
| Filtering | Performs filtering of payments (if configured). This is bank specific requirement and is performed in the site. |
| Duplicate check | Performs duplicate check on payments received from IG2 for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | The following accounting entries are raised for an inward pacs.008: **Settlement Entry (Bulk)**   - Debit clearing Nostro - Credit suspense account   **Child Transaction**   - Debit suspense account - Credit customer account |
| Error queue | Moves the inward pacs.008 failed due to format validations to error queue. |
| Repair queue | If an error occurs while processing inward pacs.008 payment (in any component in TPH STP flow), it moves the transaction to Repair queue for the user to repair or cancel the payment. The repaired payments continue with payment processing from debit account validations. If the payment is rejected from Repair queue, then TPH generates pacs.004 to IG2 clearing. |

## Outward Return (pacs.004)

TPH initiates return processing in one of the following:

- Recall request is received, and payer bank confirms to return the payment
- Credit transfer that is received can not be processed due to errors



| Activity | Description |
| --- | --- |
| Map and create return record | Creates a return record by mapping payment data from original credit transfer.  - Beneficiary party becomes the ordering party of the original transaction - Ordering party becomes the beneficiary party of the original transaction - The debit main account is the client account (as the beneficiary party of the original transaction is credited when the inward transaction is processed) - The credit main account is the outward suspense account related to the originating channel   If mapping fails, it marks the return record in error. The user can view the return record in TPH by using *Transaction Type* as RT. |
| Credit account validations | Validates whether the credit account has no posting restrictions and has sufficient balance to cover the return transaction. |
| Balance reservation | Reserves funds on the debit account (original credit account). Balance reservation is done on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Date calculation | Calculates the return payment value date and booking date, and configures it to current date (same as execution date) The return as a positive answer (the output message) is sent within the configured days to the date of cancellation request. A separate time scheduled process creates settlement transactions for outgoing return credits. |
| Routing | Routes the return payment to TPH clearing channel (IG2), which is configured to route to return HCT payment. Clearing channel then determines the return message type (pacs.004). |
| IG2 channel validations | Performs IG2 specific validations on payments to ensure that the payment meets the compliance requirements of IG2. |
| Cut-off validation | Validates IG2 final cut-off time.  To know more, refer to [IG2 HCT Cut-Off Time](#IG2_HCT_Cut-off_time) section. |
| Charge calculation | Calculates the applicable charges for positive answer to recall pacs.004 (if configured). |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is bank specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Debit posting | The following booking is generated during the processing of the return (as positive answer to recall or cancellation request):  - Debit – Client account (original amount) - Credit – Outward clearing suspense account (original amount – return charges) - Credit – P&L account (any return charges)  If the return transaction is booked successfully, it updates the status to ‘Pending to be Sent to the Clearing’. A separate time scheduled process creates settlement transactions for outgoing return credits. |
| Bulking | Bulks the transactions to batches according to bulking configuration. Single bulk can have up to 10,000 transactions. To know more, refer to [Bulking](#Bulking_Criteria) section. |
| Outward return payment generation | Generates outgoing pacs.004 message |
| Error queue | If an error occur while validating the pacs.004 message format, it moves the payment to Error queue. |
| Repair queue | If the generation of outward pacs.004 payment fails during debit account validation, reachability check, balance reservation, filtering, cut-off validations, and channel validations, it moves the return payments to Repair queue for manual action.  - If user repairs the return payment, it starts the return payment processing from debit account validations. - If user rejects the return payment in Repair queue, it sends the negative camt.029 to clearing IG2. |

## Inward Return (pacs.004)

Payee bank initiates the returns for the following:

- Request from payee
- Payee bank is unable to apply funds to the payee
- Positive response received for an outgoing recall request (camt.056)



| Activity | Description |
| --- | --- |
| Return (pacs.004) received from IG2 in TPH | Performs the following:  - Receives the return (initiated by the payee bank) for a payment that is already sent. - Receives the return when generating:   - On request of the payee   - Not able to process an inward payment (pacs.008)   - A positive response to recall request |
| Business validation | Perform the following validations for the inward pacs.004:  - Duplicate check (configurable) - Account validation - Account closed - Account stopped - Account name does not match beneficiary account number |
| Match return with payment | **Pacs.004 received for Outgoing pacs.008**  Tries to match the return with an original outward payment request (that is, returns needs to have an exact copy of the original CT). If original payment is found, it:  - Marks the original payment status as ‘Payment is being Returned’ - Creates new return payment  If original payment is not found, it:  - Moves the return to Repair queue. User can manually repair and accept or reject  **Pacs.004 received for an Outgoing Recall Request (camt.056)** Checks for associated recall request for the received pacs.004.  If associated recall request is found, it:  - Marks recall request as ‘Return in progress’ - Parks payment for posting confirmation (if configured) - Marks the Original payment status as ‘Payment is being returned’ - Creates new return payment |
| Fee processing | Enables fee component (for fee processing), and fee collection is based on configuration. |
| Value date calculation | Processes the returns on the same day it is received |
| Credit posting | Credits the payer account as part of new return payment. |
| Mark recall request and original payment status | Received pacs.004 for Outgoing pacs.008  - Updates the original payment as ‘Payment Completed with Return’  Received pacs.004 for Outgoing camt.056  - Marks the recall request as ‘Cancel Accepted’, after the confirmation from clearing (if configured) - Updates the original payment as ‘Payment completed with return’ |
| Error queue | If the validation of pacs.004 message format fail, it moves the return payment to Error queue. |
| Repair queue | Perform the following in return payment:  - If processing fails during business validations, matching with original payment and creating return payment, it moves the return payment to Repair queue for manual action.  The user can accept or reject the return payment. - If return payment is repaired, the processing starts from business validations. |

## Inward Cancellations (camt.056)

Payer bank sends cancellations (camt.056) to payee bank through IG2 clearing for an pacs.008 that is already sent. It can respond positively by sending pacs.004 or negatively by sending camt.029.



| Activity | Description |
| --- | --- |
| Receive and map recall request | Performs the following in the cancellation requests:  - Either payer bank or customer (payer) initiates the request - TPH (payee bank) receives the request for an already received payment  The following happens with the recall requests:  - TPH receives and maps the request   If the validation of recall request message format fails, it is moved to Error folder. |
| Duplicate check | Checks whether the recall request is received and then the status of the request.  - If recall request is found with status as ‘Cancel Accepted’, it sends negative response (camt.029) to payer bank. - If recall request is found with status as ‘Rejected’, it move the duplicate recall request to Repair queue for manual action. |
| Create recall request | Creates a recall request record with status as ‘Inwork’ to represent the cancellation request. |
| Match with original payment | Tries to match the cancellation request with an existing inward payment request.  - If the original payment is found, it validates whether the recall request is received within defined period (configurable). - If TPH does not find the original payment, it moves the recall request to Repair queue for manual action or rejects automatically (based on configuration).  The request needs to match the following conditions:  - Transaction amount - Settlement date - Original transaction ID |
| Validate acceptance days | Validates whether the recall request is arrived within the acceptable days (configurable).  - If the bank initiates a recall, it invokes ‘Return flow’. (The reasons can be duplicate ‘DUPL’ or fraud ‘FRAD’). - If the Customer initiates, it moves the recall request to Repair queue for manual action.  The user can accept or reject the recall request. - If the recall request is not received within the defined period, the request is moved to Manual queue for user action or auto rejected based on configuration. |
| Invoke return flow | If request is found valid, TPH invokes return processing. |
| Go to outward camt.29 flow | To know more, refer to [Outward Recall (Negative) Response (camt.029)](#Outward_Recall_(Negative)_Response_(camt.029)). |
| Error | If an error occurs in the recall requests in error, TPH generates the camt.029 (automatically). |
| Repair | If the recall request is moved to repair queue based on previous activities, the user is required to accept or reject the recall.  - If accepted, the recall processing continues. - If rejected, TPH generates the camt.029. |

## Inward Recall Response (camt.029)



| Activity | Description |
| --- | --- |
| Receive and map | Performs the following:  - Receives the recall response (camt.029) for a recall request (camt.056) that is already sent - Receives and maps the recall response   If the validation of camt.029 message fails, it moves the message to error folder. |
| Match to recall request | Tries to find the recall request for the recall response that is received.  - If the match is found, TPH validates the recall request status - If the match is not found, then ignore the recall response(camt.029) |
| Validate recall status | If recall request is already sent, it validates the cancellation overdue days. If recall request is already processed (accept or reject), it ignores further recall response. |
| Validate overdue days | Performs the following in recall response:  - If received within defined period (cancellation overdue days), it accepts the recall response. - If not received with defined period, it moves the recall response to Repair queue for manual action.   The user can accept the recall response or reject the recall response. |
| Update recall request status | If recall response is accepted, it marks the recall request status as ‘Cancel Rejected’. |

## Inward Payment Status Report (pacs.002)

Payment Status Report (PSR) received from IG2 is a processed STP or non-STP based on error codes received in PSR. If set for manual handling, the user can use appropriate enquiries to process the PSR.



| Activity | Description |
| --- | --- |
| PSR received from IG2 | Received for the following:  - File acceptance or reject - Bulk acceptance or reject - Transaction acceptance or reject  The originator bank can receive clearing status validation report for pacs.008 when validations are successful at IG2. The originator bank can receive clearing status cancellation report for camt.056 and pacs.008 as follows:  - If recall request is received for credit transfer payment, where pacs.008 is still in pending status at IG2 and not forwarded to payee bank. - If IG2 is unable to process the credit transfer request in the available clearing sessions due to reasons, such as ‘lack of funds’ or ‘suspension of either sender or receiver of CT/RCT transactions’, or ‘No clearing processing’. |
| Match with original payment | Tries to find the original payment request.  - If the match is found, it updates transaction status based on response received (accepted, rejected or partially accepted) - If the match is not found, it marks the file status as ‘Unmatched’. |
| Update payment status | Enables to process STP or non-STP (configurable). **STP Processing**   - If original payment is found and PSR status is ‘Accepted’ or ‘Rejected’, it marks the payment (automatically) as ‘Completed’ or ‘Rejected’, respectively.   **Non-STP Processing**   - If original payment is found and PSR status is ‘Accepted’, it marks the payment (automatically) as ‘Completed’. - If original payment is found and PSR status is ‘Rejected’, it parks the payment in Repair queue for manual intervention. |
| Park PSR in manual queue | Allows to Resubmit, Reject or Return the clearing status reports (Validation and Cancellation ) that are parked in Repair queue |

## Outward Recall Request (camt.056)



| Activity | Description |
| --- | --- |
| Create cancellation request (EBQA page) | Bank Operator initiates a recall request (for an already sent outward pacs.008) either as bank initiated or customer initiated recall request.  - During bank initiated recalls, the bank operator can select either ISO reason codes as ‘DUPL’ or Proprietary reason codes as TECH or FRAD - During Customer initiated recalls, the bank operator can select either ISO reason code as ‘CUST’ or Proprietary reason codes as AC03 or AM09 |
| Validate cancel acceptance days | Validates whether a cancellation request is made for a payment within defined *Acceptance Days.* If cancellation request has crossed the *Acceptance Days,* the system raises an error to the bank operator. |
| Validate channel cut-off time | Checks whether the cancellation request is made before channel cut-off time (when cancellation is sent on last day of *Acceptance Days*) If the cancellation request has crossed *Channel Cut-off Time,*  the system raises an error to the bank operator. |
| Authorise cancellation request (EBQA page) | Supervisor authorises the recall. |
| Bulking and generate camt.056 | At end of every clearing session (1 hour interval), it bulks the cancellation requests (camt.056) and send to IG2 clearing. |
| Error | If the validations fails during cancellation request creation (such as *Acceptance days, Cut-off Time* or *Negative Response*), it displays an error to the bank operator. |

## Outward Recall (Negative) Response (camt.029)



| Activity | Description |
| --- | --- |
| Recall request in manual repair queue | Handles incoming recall requests (manually) by moving it to Repair queue based on configuration (that is, auto negative cancel request response is disabled) |
| Reject recall request | Bank operator can reject the recall request based on customer consent. |
| Recall status updated | If recall request is rejected, it updates the EBQA status to indicate the rejection. |
| Bulking and generate camt.029 | At end of every clearing session (1 hour interval), it bulks the cancellation requests (camt.056) and sends to IG2 clearing. |

In this topic

- [Introduction to InterGIRO2 (IG2) Credit Transfer (CT)](#IntroductiontoInterGIRO2IG2CreditTransferCT)

- [Types of Participants](#TypesofParticipants)
- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Payment Instruments](#PaymentInstruments)
- [Bank and Account Identifier](#BankandAccountIdentifier)
- [Clearing Directory and Reachability](#ClearingDirectoryandReachability)
- [Warehouse](#Warehouse)
- [Clearing Validations](#ClearingValidations)
- [Credit Transfers](#CreditTransfers)
- [Return a Payment](#ReturnaPayment)
- [Recall a Payment](#RecallaPayment)
- [Payment Status Report](#PaymentStatusReport)
- [IG2 HCT Cut-Off Time](#IG2HCTCutOffTime)
- [Bulking Criteria](#BulkingCriteria)
- [Outward Payment Request](#OutwardPaymentRequest)
- [Inward Payment Request (pacs.008)](#InwardPaymentRequestpacs008)
- [Outward Return (pacs.004)](#OutwardReturnpacs004)
- [Inward Return (pacs.004)](#InwardReturnpacs004)
- [Inward Cancellations (camt.056)](#InwardCancellationscamt056)
- [Inward Recall Response (camt.029)](#InwardRecallResponsecamt029)
- [Inward Payment Status Report (pacs.002)](#InwardPaymentStatusReportpacs002)
- [Outward Recall Request (camt.056)](#OutwardRecallRequestcamt056)
- [Outward Recall (Negative) Response (camt.029)](#OutwardRecallNegativeResponsecamt029)

Related topics:

- [APIs](../../APIs/Misc/APIs.htm#EP)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:18:48 PM IST