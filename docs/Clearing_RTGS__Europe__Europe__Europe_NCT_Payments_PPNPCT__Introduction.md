# Introduction to Nordic Credit Transfer Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm) > Introduction

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
  - [VIBER Payments VIBER Payments](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm)
  - [MAV Payments MAV Payments](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm)
  - [Equens SEPA Direct Debit Equens SEPA Direct Debit](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm)
  - [Equens SEPA Credit Transfer Equens SEPA Credit Transfer](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm)
  - [TARGET2 Clearing (ISO20022) TARGET2 Clearing (ISO20022)](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm)
  - [Nordic Credit Transfer Payments Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
    - [Introduction](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
    - [Configuration](../../Europe/Europe_NCT_Payments_PPNPCT/Configuration.htm)
    - [Working with](../../Europe/Europe_NCT_Payments_PPNPCT/Working_with.htm)
    - [Tasks](../../Europe/Europe_NCT_Payments_PPNPCT/Tasks.htm)
    - [Outputs](../../Europe/Europe_NCT_Payments_PPNPCT/Outputs.htm)
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to Nordic Credit Transfer Payments

Updated On 08 November 2022 |
 33 Min(s) read

Feedback
Summarize

Nordic Credit Transfer (NCT) is a payment instrument used for transferring funds between two payment accounts (sending and receiving) held by banks located within the Nordic countries. The business and technical requirements of the NCT are defined and managed by the Nordic Payments Council (NPC) based on (but not limited to) the Single Euro Payments Area (SEPA) payment scheme.

The NPC Credit Transfer Scheme is a set of rules, practices and standards to achieve inter-operability for credit transfers agreed at an interbank level for the currencies covered by the Scheme. It is aimed at developing and managing additional schemes and rules with the participants, national communities and regulating authorities with a set of documents (such as, Rulebooks, Implementation Guidelines and other publications).

## Type of Participant

| Type of Participant | Description |
| --- | --- |
| Direct Participant (DP) | A member bank that exchanges payments directly with CSM and holds a settlement account with the clearing. |

## Types of Payment and Messages

TPH supports the following NCT message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.02 | B2B | Customer credit transfer | Inward and outward |
| pacs.004.001.02 | B2B | Return | Inward and outward |
| camt.056.001.01 | B2B | Payment cancellation request or request for recall | Inward and outward |
| camt.029.001.03 | B2B | Resolution of investigation | Inward and outward |
| pacs.028 | B2B | Payment status request | Inward and outward |
| pacs.002.001.03 | B2B | Clearing payment status report | Inward |
| pain.001.001.03 | C2B | Credit transfer initiation | Inward |
| pain.001.001.02 | C2B | Credit transfer initiation | Inward |
| pain.002.001.03 | B2C | Payment status report to customer | Outward |
| pain.002.001.02 | B2C | Payment status report to customer | Outward |
| pain.001.001.05 | C2B | Credit transfer initiation | Inward |
| camt.087.001.05 | B2B | Request to modify payment | Inward and outward |
| camt.027.001.06 | B2B | Claim non-receipt | Inward and outward |
| camt.029.001.08 | B2B | Resolution of investigation | Inward and outward |

## Payment Instruments

Nordic payment instrument is NCT.

## Bank Identifier Code (BIC) and IBAN

The preferred bank or branch and beneficiary account identification methods used in Nordic clearing are IBAN and BICs, respectively. As a part of the Nordic clearing regulation, NCT payment (pain.001) initiated by the customer can come without the beneficiary BIC. The beneficiary BIC is derived from the beneficiary IBAN.

## Initiating Customer Credit Transfers

NCT can be initiated using the following:

|  |  |
| --- | --- |
| pain001 | System supports both single and bulk pain.001. It can result in book (beneficiary in the books of the processing bank) or outward transfer (pacs.008 is sent to clearing). |
| Payment Order | - User needs to input ordering and beneficiary customer details, payment amount, payment currency, requested execution date or requested credit value date calculated based on payment order product configuration, which is validated and committed. - Authoriser approves the payment order, and the system processes it as a book or an outward payment depending on where the beneficiary resides. The pacs.008 message is sent to clearing for outward payments. |
| Order Entry (OE) | - User needs to input ordering and beneficiary customer details, payment amount, payment currency and debit value date in the OE page, which is validated and committed. - Authoriser approves the payment order and system processes it as a book or an outward payment depending on the residency of the beneficiary. The pacs.008 NCT reachability is sent for outward payments. |

## Receiving Incoming Credit Transfer (pacs.008)

NCT can be received from clearing, where TPH:

- Receives the pacs.008
- Performs all validations
- Uploads the pacs.008 message to the TPH tables
- Generates accounting entries as shown below.
  - Settlement entry – Bulk
    - Debit clearing Nostro
    - Credit suspense account
  - Child transactions
    - Debit suspense account
    - Customer account (will be credited in incoming credit transfer and not the suspense account)

## Returning NCT (pacs.004)

The beneficiary bank can return NCT when it cannot process the payment. For example, invalid creditor IBAN, credit account is closed, posting restrictions on the creditor account, and so on. It can be returned automatically or manually based on the following configuration:

- If a return payment is initiated, it reverses the original payment booking and moves it to the Payment Completed with Return (996) business state. It creates and sends a new return payment to clearing, which ensures to credit the Clearing Nostro.
- If a return payment is received, it processes and books the received return payment (when the original payment for the return exists). In this case, the customer who is debited (initially) gets credited. It updates the original credit transfer to Payment Completed with Return (996) business state.

## Recalling a Settled Credit Transfer (camt.056)

NCT sent to clearing (by the originator bank) can be recalled by sending a camt.056 (cancellation) recall request message (initiated by the originator or originator bank of the credit transfer). TPH can initiate a cancellation request and specify whether it is initiated by the customer or bank. The system automatically defaults the number of values from the original payment to the cancellation request and the user update a reason code stating the reason for cancellation. No accounting entries are raised for this message as it is a non-financial message. If TPH is the beneficiary bank receiving the camt.056 recall request, then it can respond with a positive answer by sending a pacs.004 return message. Return payment (pacs.004) is initiated by the following:

- Creating new return transaction
- Debiting a customer account (which was earlier credited by the incoming credit transfer)
- Creating settlement entries to credit the clearing Nostro.

The status of the original credit transfer is updated as Payment Completed with Return (996) business state. The beneficiary bank can respond with a negative response (by sending a camt.029 Resolution of Investigation (ROI) message) indicating the rejection of recall request received from the originator bank. It is a non-financial message that:

- Has no accounting entries raised during the process.
- Is initiated when the reason code for rejection is entered.

The response to an incoming cancellation request can be initiated manually or automatically. When the beneficiary bank receives the recall request, it retrieves the original credit transfer payment for which the recall has been received.

- If the original transaction is not found, the cancellation request is rejected automatically based on the configuration.
- If the original credit transfer details are retrieved, the system checks whether the cancellation request can be processed automatically based on the configuration.

- If the *AutoReturnIndicator* flag is set to N, it parks the cancellation request for manual action.
- If not, it processes the cancellation request automatically to return the original credit transfer by using pacs.004.
- If a customer initiates a cancellation request, the system checks whether it is within the acceptance days. Otherwise, it is rejected by sending camt.029 message.

- If a customer initiates a cancellation request, the system checks whether it is within the acceptance days. Otherwise, it is rejected by sending camt.029 message.

If it is within the acceptance days, the return processing of the original credit transfer is done either manually or automatically based on configuration.

- The acceptance day’s check to initiate a cancellation request can be configured separately for customer and bank-initiated recall requests.

## Initiating a Bulk Recall Request (camt.056)

TPH can initiate a bulk cancellation request by selecting multiple credit transfers. If the reason code for the cancellation request is provided and bulk cancellation request is authorised, the camt.056 message is generated.

## Requesting for Status Update (pacs.028)

This message (non-financial) is sent to enquire the status of the cancellation request (camt.056). The originator bank can initiate this request from the enquiry provided. When the beneficiary bank receives a request for status update (pacs.028), it performs the following:

- If the recall request is already accepted (that is, a return payment is sent to the originator bank), it generates a camt.029 (negative response) with ‘ADRT’ status as a response.
- If the recall request is already rejected (that is, a camt.029 is sent to the originator bank), it generates a camt.029 (negative response) with the original reject reason code as a response.

The ordering bank can send a request for status update (pacs.028) for camt.27 and camt.87, and the beneficiary bank can receive and process it. Additionally, it can send a request to the beneficiary bank for status update of an inquiry for which they have not received any response.

| Status Update | Description |
| --- | --- |
| Outgoing Request | Provides the user with an enquiry to initiate a status update request (pacs.028) for an outgoing camt.027 or camt.087. |
| Incoming Request | When an incoming request for status update is received, the system checks for camt.027 or camt.087 request from the originator bank.  - If a matching record is not available, the system updates the status to ‘Unmatched’. - If a matching record is found, the system checks whether camt.029 response is sent as a response for the incoming camt.027 or camt.087.   - If camt.029 response is sent already, the same is sent again (automatically) with a new case ID to avoid duplicate check.   - If camt.029 response is not sent, the user can initiate the response (manually) from the enquiry. |

## Claiming for Non-Receipt by Originator (camt.027.001.06)

A message type for the originator or beneficiary of the payment, to send or receive a claim of non-receipt of initial credit transfer. This is performed when the beneficiary claiming non-receipt contacts the user.

| Message Type | Description |
| --- | --- |
| Outgoing camt.027 | Provides the user with an enquiry to initiate a camt.027. This enquiry lists all the outgoing pacs.008 in completed status, which are sent to clearing.  - When initiating the camt.027 from the enquiry, the system checks for request that is initiated within 13 months of the original credit transfer.   - If initiated outside the parameterised time frame, it displays an error message and does not allow the user to initiate the camt.027 request. |
| Incoming camt.027 | - Processes and uploads the incoming camt.027 message - Provides the enquiry to the user to view the incoming camt.027 message - System matches the incoming camt.027 with the original pacs.008, which is already processed.   - If the original payment is found and is in a completed state, the system automatically (configuration) generates camt.029 with status code as ACNR. Also, places the acceptance date of the camt.027 claim and maps the process in the outgoing camt.029 (v8.0).   - If the original payment is found and is in ‘Cancelled, Rejected and Returned’ status, the system automatically generates (configuration) camt.029 with status code as RJNR and reason code as ARDT in the outgoing camt.029.   - If the original payment is not found, the system automatically rejects the camt.029 (v8.0) with reason code as NOOR and status as ‘RJNR’.   - If the original payment is not found and the system is configured for manual action, it parks the camt.027 to Unmatched queue for manual action.   The user needs to perform the following, when camt.027 is parked for manual action:  - Initiate the camt.029 (v.8) message from the enquiry in response to an incoming camt.027. - Perform additional check whether the incoming camt.027 is responded by the beneficiary bank within 10 days of the receipt of the camt.027 message. - Map and bulk the outgoing camt.029 (v8.0), and generate the file in the output folder. |

## Claiming for Value Date Correction or Requesting to Modify Payment (camt.087.001.05)

A message type introduced as part of the originator or beneficiary of the payment to send or receive a value date confirmation or modification request of initial credit transfer. This is performed when the beneficiary (claiming non-receipt of funds) contacts on the intended value date. The incoming camt.087 message indicates a modification in the payment due to change in the interbank settlement date.

| Message Type | Description |
| --- | --- |
| Outgoing camt.087 | Provides the user with an enquiry to initiate a camt.087. The enquiry lists all the outgoing pacs.008 in ‘Completed’ status, which are sent to clearing.  - When initiating the camt.087 from the enquiry, the system checks whether the request is initiated within 13 months of the original credit transfer.   - If initiated outside the parameterised timeframe, it displays an error message and does not allow the user to initiate the camt.087.   The modified *Interbank Settlement Date* field is defaulted with original credit value date of outgoing pacs.008.  - If there is no change in the modified interbank settlement date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become mandatory. - If the user changes the date in modified *Interbank Settlement* field to a new date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become non-mandatory.  Updates the status of camt.087 to ‘Claim Sent’ status in TPH. Additionally, it bulks the outgoing camt.027 and generates it in the outgoing message folder |
| Incoming camt.087 | System performs the following when the beneficiary bank receives a camt.087 message:  - Processes and uploads the incoming camt.087 message. - Provides the enquiry to the user to view the incoming camt.087 message. - Matches the incoming camt.087 with the original pacs.008, which are already processed.   - If the original payment is not found, the system updates the status to ‘Unmatched’.   - If the original payment is found, the system checks whether camt.087 is received within the acceptance days.   - - If yes, it proceeds with Straight-Through Processing (STP) of the camt.087 message     - If not, it parks the incoming camt.087 for manual intervention   - If the original payment is found and is within acceptance days, system checks whether the original payment is in ‘Completed’ status.   - - If yes, it proceeds with STP of the camt.087 message.     - If not, it updates the incoming camt.087 status as ‘Invalid Claim’. The claim is invalid as the original payment is returned already and does not allow to modify the date in the original payment. Hence, the user cannot perform any manual action as the claim is set as ‘Invalid’.   - If the original payment is in ‘Completed’ status and *Automated Return Indicator* is set to Yes, the system checks whether the modified and original credit value date of pacs.008 transaction is same.   - - If the dates are not same, it parks the camt.087 request for manual action and updates the status to ‘Inwork’.     - If the dates are same, it automatically generates the camt.029 with status as ‘RJVA’ |

## Supporting Extended Remittance Information

When a pain.001 file is received with both structured and unstructured information, the details are stored in the TPH table and rulebook local instrument code is available with PERI. The system checks the beneficiary bank BIC that supports ERI payment option (based on which the structured and unstructured information are mapped in the outgoing pacs.008 message) before generating the pacs.008 message to clearing. TPH system performs validation to update the local instrument code PERI received in the pain.001 file in the respective TPH table. The reachability API checks whether the beneficiary bank supports ERI option based on the information from the routing table. During validation, it checks for the total character length of 280 characters for structured tags in ERI payment option.

- If the incoming pain.001 does not have the local instrument code as PERI, it updates in the TPH table based on reachability API check.
- If the API return the value ERI, it updates the local instrument code as PERI in TPH.

| Scenario | Tag |
| --- | --- |
| **Outward pacs.008 Mapping** | |
| Local instrument code is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code is equal to PERI | Maps max 999 occurrences with all structured remittance tags |
| **Outward R-messages Mapping** (pacs.004, pacs.028, camt.056, camt.029, camt.029(v8.0), camt.027, camt.087) | |
| Local instrument code in POR.SupplementaryInfo of original transaction is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is equal to PERI | Does not map any remittance information |

While initiating and sending outgoing camt.056, pacs.004, camt.029 and pacs.028, the system checks the original payment (pacs.008) for the local instrument code.

- If it has PERI, the structured information is not sent in the outgoing camt.056, pacs.004, camt.029, camt.027, camt.087 and pacs.028.

While receiving pacs.008 message from clearing, it maps the local instrument code PERI to the respective TPH table and stores the structured remittance information in the remittance information table in TPH.

## Order Entry (OE) and Payment Order (PO) Application

Extended Remittance Information (ERI) allows participant bank users in entering details (upto 999 occurrences) of structured remittance information when initiating CT from Payment Initiation (PI) pages. It is enhanced to split the information (based on the European Payments Council (EPC) guideline), when there are more than 280 characters (inclusive of business and service content). This populates the additional characters in subsequent structured remittance information occurrences while sending an outgoing message to clearing. Nordic CT PI version pages (in PO and OE) perform certain validations based on the occurrences, before accepting the payments initiated by the user.

## Bulking Criteria

A file sent to Nordic Clearing contains only message type per file. Multiple message types cannot be bulked in one file. The pacs.008, pacs.004, camt.056 and camt.029 messages are sent in separate files to the clearing.

## Retrieving Original Credit Transfer

During an incoming return, when a camt.056 or camt.029 message is received, the original credit transfer message is retrieved based on the following conditions:

- Transaction amount
- Settlement date
- Original transaction ID in the R-transaction against transaction ID (original payment)

## Handling Payment Status Report (PSR) - pacs.002s2

The pacs.002s2 clearing status report for the NCT messages sent to clearing (pacs.008, pacs.004, camt.056, camt.029, camt.027, camt.087 and camt.029 -v8.0) is sent to the originator bank. The payment clearing status report (pacs.002s2) can be classified into three types of acceptances and rejections:

| Level | Description |
| --- | --- |
| File level | A complete file acceptance or rejection. |
| Bulk level | A bulk-level acceptance or rejection of the outward credit transfer message sent to the clearing.  - Some bulks are fully accepted or rejected - Some payments within the file are accepted while others are rejected |
| Transaction level | The information on the number of transactions accepted and rejected inside the bulk. Payment information details are provided for the rejected transactions. |

The clearing status report received can be a processed STP or Non-STP. It is parked for manual action based on the reason code in the incoming pacs.002s2 (configure the *RouteToException* field to Yes). The user can take manual actions, such as resubmit, reject or return the transaction from the Sent Exception page. The user can resubmit or reinitiate the clearing of rejected camt.027, camt.087 or camt.029 (v8.0) message from the enquiry again.

[Receiving Clearing Status Report (pacs.002s2) and Forwarding to Indirect Participant Bank](#)

When a pacs.002S2 reject message is received for an outgoing pacs.008, pacs.004, camt.056 (cancellation request) and camt.029 (resolution of investigation) originated from IP (based on the parameterisation in TPH), it moves the rejected transactions to the Sent Exception page for manual intervention. This enables the bank users to perform the following actions:

| Action | Description |
| --- | --- |
| Resubmit | The user performs the following actions:  - Cannot resubmit the camt.056 or camt.029 message to the clearing, as it displays an error message - Can resubmit the pacs.008 or pacs.004 message to the clearing |
| Return or Reverse | The clearing performs the following:  - Rejected pacs.004, camt.056 or camt.029 is forwarded as pacs.002s2 to the IP - Rejected pacs.008 is sent as pacs.004 to the IP |

## Enquiry to View the Sent or Received Credit Transfer File

TPH has the enquiries to view all the Direct Debit (DD) or Credit Transfer (CT) files received from IP or clearing channel. The user can navigate to the bulk level enquiry from the file level enquiry and further transaction level enquiry.

## Enquiry to View Unmatched R-Messages

- To list the CT return transactions (pacs.004) in repair status (status code - 235) with ‘Original Transaction is Not Found Error’ or ‘Transaction Not in Completed’ status, go to Payment Inquiries>Pending Payments>Pending Unmatched R-Payments Enquiry.
- Enter the FT number of the original transaction in the *Original Transaction Reference* field, when releasing the payment from general repair queue or new inquiry.

- This field is mapped to *OriginalorReturnId* field in `POR.SUPPLEMENTARY.INFO` table.
- TPH validates whether the entered FT number exists in the system and is in ‘Completed’ status.
- Additionally, allows to release the transaction from repair without entering the original transaction reference (when original transaction is not migrated from legacy system to TPH).

## Outward Processing – Payment Request (pacs.008)

Payment can be initiated from Payment Order, Order Entry or through a pain.001 file (message initiated by a customer). The below diagram shows the processing activities involved in the payment flow sequence.



| Activity | Description |
| --- | --- |
| Manual Capture of NCT payment from branch or back-office using `PO` application | Captures a NCT payment from `PO` application. Validates mandatory and non-mandatory fields on submission and displays errors (if any). |
| Payment initiation using pain.001 message | Initiates a NCT by sending a pain.001 (EPC standard) message to the ordering bank. |
| Receiving and mapping | Receives, validates and maps the pain.001 message. The pain.001 message can have one or more customer batches. If pain.001 message format validation fails, it is moved to the Error queue. To check bulk agreements, the system validates whether the submitter or issuer (debtor) has an agreement to send the pain.001 file. If the bulk agreement validation fails, it moves the file to the Error queue. |
| Debulking | If pain.001 is a batch payment, it is debulked to single transactions. Based on the batch indicator in the file (pain.001) or the bulk agreement, the system decides whether the transactions in the bulk needs to be processed as individual transactions (single debit – single credit) or batch (single debit – multiple credits). |
| Warehouse (level 1) | Warehouses payments with future requested execution date and releases on the Start of Day (SOD) of the execution date. |
| Account validations | Validates whether the ordering account is a valid Temenos Transact account |
| Balance check without charges | Checks whether the debit account has no posting restrictions and has funds to process a payment.  Performs balance reservation on the payment amount without charges, and is applicable when the Account Management System (AMS) is Temenos Transact (embedded mode). |
| Routing | Routes the payment to a Nordic clearing channel which is configured to route to NCT payment. Clearing channel determines the message type (pacs.008). |
| Reachability check | Validates whether the beneficiary bank is reachable through the selected Nordic CSM directly or indirectly (if configured). |
| Nordic channel validations | Validates whether the payment meets the compliance requirements of NCT scheme (such as IBAN is mandatory and valid, address details available, currency is EUR, and charge option is SHA). |
| Cut-off validation | Validates whether the NCT is before final cut-off time of the settlement date. TPH calculates the settlement date (credit value date) and execution date based on the cut-off time defined for the Nordic CSM. If the payment passes the cut-off time, it moves the execution date to the next business day. |
| Dates calculation | Calculates the remaining dates, such as book date, debit value date (floats are configurable) and send date (configurable). Booking date is equal to the processing date. Send date is configured to be equal to the settlement date (credit value date). Debit value date is configured based on processing date considering configured floats. |
| Duplicate check | Performs duplicate check on payment amount, currency and transaction reference. |
| FATF and WTR2 validations | Validates whether the necessary details are available in the payment instruction according to FATF and WTR2 regulation. This is applicable when FATF validation is enabled in the system. |
| Submission and supervisor approval | Performs the following validations:  - On submission of the payment, it waits for Supervisor’s approval. - Once approved, it is moved for further processing.  If rejected, it is modified and resubmitted for approval. It is then sent to Temenos Payments Hub Engine for further processing. Payments received in TPH from external banks in STP mode do not wait for Supervisor’s approval. |
| Sanction screening | Performs sanction screening of payments when interfaced to a screening engine. This is a bank-specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos Financial Crime Mitigation (FCM) solution. |
| Warehouse (level 2) | Warehouses payments with future determined execution date (missed the final cut-off for the current business date). |
| Fee calculation | Calculates the applicable charges (if configured) |
| Balance reservation | Reserves funds on the debit account and checks whether the debit account has no posting restrictions. It is done on payment amount with charges.  - If AMS is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Posting | Debits the payment amount and any charges to be borne by the customer to the debtor account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (reject, cancel or automatic retry) based on the configuration.  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward payments are entries made before sending pacs.008 to clearing  - Credit transaction entries (single accounting)  - Debit debtor account - Credit CSM suspense Account  - Credit transaction entries (single debit – multiple credit accounting)  Total batch amount  - Debit debtor account - Credit batch suspense account  Individual transactions in the batch  - Batch suspense account - Credit CSM suspense account |
| Park for distribution | Parks the payment after raising the accounting entries. The payments are sent to the CSM at pre-defined frequency (defined for credit transfers) based on the settlement cycles. |
| Bulking | Bulks the transactions into batches according to bulking configuration defined for the CSM (including file and bulk naming convention, number of bulks in a file, number of transactions in a bulk). Credit transfers for the CSM are bulked based on settlement date (credit value date). Each outgoing transaction has a bulk reference (as part of the payment details), which can be viewed from the Payments Inquiry page. |
| Outward payment generation | Generates pacs.008 message at the end of every clearing settlement cycle (configured as per CSM and message type). Each CSM can have its own XSD and mapping requirements. Settlement transaction is created in the system for each bulk in the outgoing file. Settlement Transaction accounting entries   - Debit CSM suspense account - Credit CSM nostro account |
| Send customer status report | Sends a notification to the customer in the agreed format (pain.002, etc.) about the success or failure of the payment execution. |
| Error queue | If message format validations fail for pain.001 batches, it parks the payment in the Error queue. This can be viewed from TPH Received Files Enquiry page |
| Repair queue | If an outward pacs.008 payment generation fails in any component of TPH STP flow, it moves to the Repair queue. The user can repair or cancel the payment. Repaired payments continue with payment processing starting from debit account validations. |

## Inward Processing – Payment Request (pacs.008)



| Activity | Description |
| --- | --- |
| NCT Payment Received from clearing | Receives an inward payment pacs.008 from clearing in TPH. Beneficiary bank can receive pacs.008 or a mix of all message types (pacs.008, pacs.004) in a SCF file from the CSM (based on CSM service and agreement with the CSM). |
| Nordic specific format validations | Performs schema validation on the payment according to the XSD of the CSM. If validation fails, it moves the message to the Error queue. |
| Debulking and mapping | Credit transfer transaction (CT transaction type) is created for each record in the bulk. A settlement transaction is created for the total amount for each pacs.008 bulk in the file. |
| Account validation | Validates the beneficiary account for the following:  - Invalid - Restrictions - Account type does not allow to credit external transfer items (product configuration) - Closed - Blocked with a specific code (such as criminal block) |
| Dates calculation | Calculates the settlement and processing dates. The settlement date of the payments received from Nordic CSM can be in the past and not in the future.  - Processing date is the current business date - Debit value date is the settlement date available in the instruction - Credit value date is the processing date along with credit floats (as agreed with the customer) |
| Duplicate check | Performs duplicate check on payments received from Nordic CSM for the configured set of payment attributes. |
| FATF and WTR2 validations | Validates whether the necessary details are available in the payment instruction according to the FATF and WTR2 regulation. This is applicable when FATF validation is enabled in the system. |
| Sanction screening | Performs sanction screening of payments (if configured). This is a bank-specific requirement and is performed in the site. |
| FX | Performs FX when the credit account currency is different from transaction currency. |
| Fee calculation | Calculates and collects the fee in TPH based on configuration. NCT scheme does not define any interchange fees. Hence, there is no generic charge setup in the system by default and charge option is always SHA. Charges (applicable to the customer) are configured, according to the bank agreement with the customer, and are debited in addition to the transaction amount. |
| Credit posting | Raises the following accounting entries for an inward pacs.008:  - Settlement entry (bulk)  - Debit clearing Nostro (Value date is equal to settlement date in the file) - Credit suspense account (Value date is equal to settlement date in the file)  - Individual transaction  - Debit suspense account (Value date is equal to settlement date in the file) - Credit customer account (Value date =Current business date + Floats) |
| Credit advice | Generates any credit advice (through FAX, email) agreed with the customer. |
| Error queue | If the inward pacs.008 fails due to format validations, it moves to the Error queue. This can be viewed from TP Received Files Enquiry page. |
| Repair queue | If inward pacs.008 payment processing fails in any component in TPH, STP flow goes to the Repair queue (if automatic return is not configured). User can repair, return or cancel the payment. Repaired payments continue with payment processing from debit account validations. If the payment is returned from the Repair queue, then TPH generates a pacs.004 to Nordic CSM. |

In this topic

- [Introduction to Nordic Credit Transfer Payments](#IntroductiontoNordicCreditTransferPayments)

- [Type of Participant](#TypeofParticipant)
- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Payment Instruments](#PaymentInstruments)
- [Bank Identifier Code (BIC) and IBAN](#BankIdentifierCodeBICandIBAN)
- [Initiating Customer Credit Transfers](#InitiatingCustomerCreditTransfers)
- [Receiving Incoming Credit Transfer (pacs.008)](#ReceivingIncomingCreditTransferpacs008)
- [Returning NCT (pacs.004)](#ReturningNCTpacs004)
- [Recalling a Settled Credit Transfer (camt.056)](#RecallingaSettledCreditTransfercamt056)
- [Initiating a Bulk Recall Request (camt.056)](#InitiatingaBulkRecallRequestcamt056)
- [Requesting for Status Update (pacs.028)](#RequestingforStatusUpdatepacs028)
- [Claiming for Non-Receipt by Originator (camt.027.001.06)](#ClaimingforNonReceiptbyOriginatorcamt02700106)
- [Claiming for Value Date Correction or Requesting to Modify Payment (camt.087.001.05)](#ClaimingforValueDateCorrectionorRequestingtoModifyPaymentcamt08700105)
- [Supporting Extended Remittance Information](#SupportingExtendedRemittanceInformation)
- [Order Entry (OE) and Payment Order (PO) Application](#OrderEntryOEandPaymentOrderPOApplication)
- [Bulking Criteria](#BulkingCriteria)
- [Retrieving Original Credit Transfer](#RetrievingOriginalCreditTransfer)
- [Handling Payment Status Report (PSR) - pacs.002s2](#HandlingPaymentStatusReportPSRpacs002s2)
- [Enquiry to View the Sent or Received Credit Transfer File](#EnquirytoViewtheSentorReceivedCreditTransferFile)
- [Enquiry to View Unmatched R-Messages](#EnquirytoViewUnmatchedRMessages)
- [Outward Processing – Payment Request (pacs.008)](#OutwardProcessingPaymentRequestpacs008)
- [Inward Processing – Payment Request (pacs.008)](#InwardProcessingPaymentRequestpacs008)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:57 PM IST