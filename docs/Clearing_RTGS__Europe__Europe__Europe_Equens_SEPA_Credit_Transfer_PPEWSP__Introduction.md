# Introduction to Equens SEPA Credit Transfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Equens SEPA Credit Transfer](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm) > Introduction

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
    - [Introduction](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm)
    - [Configuration](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Configuration.htm)
    - [Working with](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Working_with.htm)
    - [Tasks](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Tasks.htm)
    - [Outputs](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Outputs.htm)
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

# Introduction to Equens SEPA Credit Transfer

Updated On 20 January 2026 |
 36 Min(s) read

Feedback
Summarize

The Single Euro Payments Area (SEPA) is an initiative to create a zone for the Euro, where:

- All electronic payments are considered domestic.
- Difference between national and Intra-European cross-border payments does not exist.

The project aims to improve the efficiency of cross-border payments and convert the fragmented national markets for Euro payments to single domestic. It enables the customer to make cashless Euro payments to any person located anywhere by using a single bank account and single set of payment instruments. SEPA Credit Transfer (SCT) allows transfer of funds from one bank account to another. SEPA clearing rules require the payments that are made before the cut-off point on a working day, hence, it can be credited to the recipients account within one working day.

The Equens SEPA Credit Transfer (SCT) is a payment instrument in Euro used to transfer funds between two payment accounts held by banks located within Netherlands (NL). It needs to have both the sending and receiving accounts registered with banks (or bank branches) located in NL. The Equens Credit Transfer (CT) has to follow a common set of rules, practices and message formats defined by the Equens Worldline.

[Type of Participant](#)

There is only one type of participant in Equens SCT.

| Type of Participant | Description |
| --- | --- |
| Direct Member | A participant bank that exchanges payments directly to the clearing (EBA, Equens, RPSSCL) and holds a settlement account with clearing. |

TPH can be configured to act as SEPA direct participant that directly interacts with SEPA clearing house.

[Types of Payment and Messages](#)

TPH supports the following SCT message types:

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

[Payment Instruments](#)

SEPA payment instrument is SCT.

[Bank Identifier Code (BIC) and IBAN](#)

The preferred bank or branch and beneficiary account identification methods used in SEPA are IBAN and BICs, respectively. As a part of SEPA regulation, SCT payment (pain.001) initiated by the customer can come without the beneficiary BIC. The beneficiary BIC is derived from the beneficiary IBAN.

[Initiating Customer Credit Transfers](#)

Equens SCT can be initiated using the following:

|  |  |
| --- | --- |
| pain001 | System supports both single and bulk pain.001. It can result in book (beneficiary in the books of the processing bank) or outward transfer (pacs.008 is sent to clearing). |
| Payment Order | - User needs to input ordering and beneficiary customer details, payment amount, payment currency, requested execution date or requested credit value date calculated based on payment order product configuration, which is validated and committed. - Authoriser approves the payment order, and the system processes it as a book or an outward payment depending on where the beneficiary resides. The pacs.008 message is sent to clearing for outward payments. |
| Order Entry (OE) | - User needs to input ordering and beneficiary customer details, payment amount, payment currency and debit value date in the OE page, which is validated and committed. - Authoriser approves the payment order and system processes it as a book or an outward payment depending on the residency of the beneficiary. The pacs.008 SCT reachability is sent for outward payments. |

SEPA clearing house provides the SEPA routing directory file and uploads it to the `CA.CLEARING.DIRECTORY` table in TPH. System decides whether the beneficiary BIC is reachable based on the following conditions:

- Belongs to the SCT scheme.
- Status of the participant as ‘Enabled’.
- Start date indicates the date from which the BIC becomes active and can be used in SEPA payments.
- End date indicates the date after which the BIC cannot participate in SEPA payments.

[SEPA CT Cut-Off Time](#)

The SCT payments can be sent to the EBA clearing, three days prior to the requested credit value date. Hence, EBA clearing does not accept any SCT payment that is received before this time period.

[Receiving Incoming Credit Transfer (pacs.008)](#)

The SCT can be received from clearing, where TPH:

- Receives the pacs.008
- Performs all validations
- Uploads the pacs.008 message to the TPH tables
- Generates accounting entries as shown below.

- Settlement entry – Bulk

- Debit clearing Nostro
- Credit suspense account

- Child transactions

- Debit suspense account
- Credit customer account

[Returning Equens SCT (pacs.004)](#)

The beneficiary bank can return SCT when it cannot process payment. For example, invalid creditor IBAN, credit account is closed, posting restrictions on the creditor account, and so on. It can be returned automatically or manually based on the following configuration:

- If a return payment is initiated, it reverses the original payment booking and moves it to the Payment Completed with Return (996) business state. It creates and sends a new return payment to clearing, which ensures to credit the Clearing Nostro.
- If a return payment is received, it processes and books the received return payment (when the original payment for the return exists). In this case, the customer who is debited (initially) gets credited. It updates the original credit transfer to Payment Completed with Return (996) business state.

[Recalling a Settled Credit Transfer (camt.056)](#)

SCT sent to clearing (by the originator bank) can be recalled by sending a camt.056 (cancellation) recall request message (initiated by the originator or originator bank of the credit transfer). TPH can initiate a cancellation request and specify whether it is initiated by the customer or bank. The system automatically defaults the number of values from the original payment to the cancellation request and the user updates a reason code stating the reason for cancellation. No accounting entries are raised for this message as it is a non-financial message. If TPH is the beneficiary bank receiving the camt.056 recall request, then it can respond with a positive answer by sending a pacs.004 return message. Return payment (pacs.004) is initiated by the following:

- Creating new return transaction
- Debiting a customer account (which was earlier credited by the incoming credit transfer)
- Creating settlement entries to credit the clearing Nostro.

The status of the original credit transfer is updated as 'Payment Completed with Return' (996) business state. The beneficiary bank can respond with a negative response (by sending a camt.029 Resolution of Investigation (ROI) message) indicating the rejection of recall request received from the originator bank. It is a non-financial message that:

- Has no accounting entries raised during the process.
- Is initiated when the reason code for rejection is entered.

The response to an incoming cancellation request can be initiated manually or automatically. When the beneficiary bank receives the recall request, it retrieves the original credit transfer payment for which the recall has been received.

- If the original transaction is not found, the cancellation request is rejected automatically based on the configuration.
- If the original credit transfer details are retrieved, the system checks whether the cancellation request can be processed automatically based on the configuration.

[ Example](#)

- If the *Auto Return Indicator* flag is set to N, it parks the cancellation request for manual action.
- If not, it processes the cancellation request automatically to return the original credit transfer by using pacs.004.

- If a customer initiates a cancellation request, the system checks whether it is within the acceptance days. Otherwise, it is rejected by sending camt.029 message.

If it is within the acceptance days, the return processing of the original credit transfer is done either manually or automatically based on configuration.

- The acceptance day’s check to initiate a cancellation request can be configured separately for customer and bank initiated recall requests.

[Initiating a Bulk Recall Request (camt.056)](#)

TPH can initiate a bulk cancellation request by selecting multiple credit transfers. If the reason code for the cancellation request is provided and bulk cancellation request is authorised, the camt.056 message is generated.

[Requesting for Status Update (pacs.028)](#)

This message (non-financial) is sent to enquire the status of the cancellation request (camt.056). The originator bank can initiate this request from the enquiry provided. When the beneficiary bank receives a request for status update (pacs.028), it performs the following:

- If the recall request is already accepted (that is, a return payment is sent to the originator bank), it generates a camt.029 (negative response) with 'ADRT' status as a response.
- If the recall request is already rejected (that is, a camt.029 is sent to the originator bank), it generates a camt.029 (negative response) with the original reject reason code as a response.

The ordering bank can send a request for status update (pacs.028) for camt.27 and camt.87, and the beneficiary bank can receive and process it. Additionally, it can send a request to the beneficiary bank for status update of an inquiry for which they have not received any response.

| Status Update | Description |
| --- | --- |
| Outgoing Request | Provides the user with an enquiry to initiate a status update request (pacs.028) for an outgoing camt.027 or camt.087. |
| Incoming Request | When an incoming request for status update is received, the system checks for camt.027 or camt.087 request from the originator bank.   - If a matching record   is not available, the system updates the status to 'Unmatched'. - If a matching record   is found, the system checks whether camt.029 response is sent as a   response for the incoming camt.027 or camt.087.   - If camt.029 response is sent already, the same is sent     again (automatically) with a new case ID to avoid duplicate check.   - If camt.029 response is not sent, the user can initiate     the response (manually) from the enquiry. |

[Claiming for Non-Receipt by Originator (camt.027.001.06)](#)

A new message type is introduced as part of SEPA 2019 changes for the originator or beneficiary of the payment to send or receive a claim of non-receipt of initial credit transfer. This is performed when the beneficiary claiming non-receipt contacts the user.

| Message Type | Description |
| --- | --- |
| Outgoing camt.027 | Provides the user with an enquiry to initiate a camt.027. This enquiry lists all the outgoing pacs.008 in 'Completed' status, which are sent to clearing.   - When initiating the   camt.027 from the enquiry, the system checks for request that is initiated   within 13 months of the original credit transfer.   - If     initiated outside the parameterised time frame, it displays an error message and     does not allow the user to initiate the camt.027 request. |
| Incoming camt.027 | - Processes and   uploads the incoming camt.027 message - Provides the enquiry   to the user to view the incoming camt.027 message - System matches the   incoming camt.027 with the original pacs.008, which is already processed.   - If the original payment is found and is in a completed     state, the system automatically (configuration) generates camt.029 with     status code as 'ACNR'. Also, places the acceptance date of the camt.027 claim and     maps the process in the outgoing camt.029 (v8.0).   - If the original payment is found and is in 'Cancelled,     Rejected and Returned' status, the system automatically generates (configuration)     camt.029 with status code as RJNR and reason code as ARDT in the outgoing     camt.029.   - If the original payment is not found, the system automatically     rejects the camt.029 (v8.0) with reason code as NOOR and status as 'RJNR'.   - If the original payment is not found and the system is     configured for manual action, it parks the camt.027 to Unmatched queue for     manual action.   The user needs to perform the following, when camt.027 is parked for manual action:  - Initiate the camt.029   (v.8) message from the enquiry in response to an incoming camt.027. - Perform additional   check whether the incoming camt.027 is responded by the beneficiary bank   within 10 days of the receipt of the camt.027 message. - Map and bulk the   outgoing camt.029 (v8.0), and generate the file in the output folder. |

[Claiming for Value Date Correction or Requesting to Modify Payment (camt.087.001.05)](#)

A new message type introduced as part of SEPA 2019 changes for the originator or beneficiary of the payment to send or receive a value date confirmation or modification request of initial credit transfer. This is performed when the beneficiary (claiming non-receipt of funds) contacts on the intended value date. The incoming camt.087 message indicates a modification in the payment due to change in the interbank settlement date.

| Message Type | Description |
| --- | --- |
| Outgoing camt.087 | Provides the user with an enquiry to initiate a camt.087. The enquiry lists all the outgoing pacs.008 in 'Completed' status, which are sent to clearing.   - When initiating the   camt.087 from the enquiry, the system checks whether the request is initiated   within 13 months of the original credit transfer.   - If initiated outside the parameterised timeframe, it     displays an error message and does not allow the user to initiate the     camt.087.    The   modified *Interbank Settlement Date* field   is defaulted with original credit value date of outgoing pacs.008.   - If there is no change in the modified interbank     settlement date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become mandatory.   - If the user changes the date in modified *Interbank Settlement* field to a new     date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become     non-mandatory.   Updates the status of camt.087 to 'Claim Sent' status in TPH. Additionally, it bulks the outgoing camt.027 and generates it in the outgoing message folder |
| Incoming camt.087 | System performs the following when the beneficiary bank receives a camt.087 message:   - Processes and uploads the incoming camt.087 message - Provides the enquiry to the user to view the incoming camt.087 message. - Matches the incoming camt.087 with the original pacs.008, which are already processed   - If the original payment is not found, the system updates the status to 'Unmatched'.   - If the original payment is found, the system checks whether camt.087 is received within the acceptance days.    - If yes, it proceeds with Straight-Through Processing (STP) of the camt.087 message   - If not, it parks the incoming camt.087 for manual intervention   - If the original payment is found and is within acceptance days, system checks whether the original payment is in 'Completed' status.    - If yes, it proceeds with STP of the camt.087 message   - If not, it updates the incoming camt.087 status as 'Invalid Claim'. The claim is invalid as the original payment is returned already and does not allow to modify the date in the original payment. Hence, the user cannot perform any manual action as the claim is set as Invalid.   - If the original payment is in 'Completed' status and *Automated Return Indicator* is set to Yes, the system checks whether the modified and original credit value date of pacs.008 transaction is same.    - If the dates are not same, it parks the camt.087 request i for manual action and updates the status to 'Inwork'.   - If the dates are same, it automatically generates the camt.029 with status as 'RJVA'. |

[Supporting Extended Remittance Information](#)

When a pain.001 file is received with both structured and unstructured information, the details are stored in the TPH table and rulebook local instrument code is available with PERI. The system checks the beneficiary bank BIC that supports ERI payment option (based on which the structured and unstructured information are mapped in the outgoing pacs.008 message) before generating the pacs.008 message to clearing. TPH system performs validation to update the local instrument code PERI received in the pain.001 file in the respective TPH table. The reachability API checks whether the beneficiary bank supports ERI option based on the information from the STEP2 routing table. During validation, it checks for the total character length of 280 characters for structured tags in ERI payment option.

- If the incoming pain.001 does not have the local instrument code as PERI, it updates in the TPH table based on reachability API check.
- If the API return the value ERI, it updates the local instrument code as PERI in TPH.

| Scenario | Tag |
| --- | --- |
| **Outward pacs.008 Mapping** | |
| Local Instrument Code is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code is equal to PERI | Maps max 999 occurrences with all structured remittance tags |
| **Outward R-messages Mapping** (pacs.004, pacs.028, camt.056, camt.029, camt.029(v8.0), camt.027, camt.087) | |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is equal to PERI | Does not map any remittance information |

While initiating and sending outgoing camt.056, pacs.004, camt.029 and pacs.028, the system checks the original payment (pacs.008) for the local instrument code.

- If it has PERI, the structured information is not sent in the outgoing camt.056, pacs.004, camt.029, camt.027, camt.087 and pacs.028.

While receiving pacs.008 message from clearing, it maps the local instrument code PERI to the respective TPH table and stores the structured remittance information in the remittance information table in TPH.

[](#)[Order Entry (OE) and Payment Order (`PO`) Application](#)

Extended Remittance Information (ERI) allows participant bank users in entering details (upto 999 occurrences) of structured remittance information when initiating CT from Payment Initiation (PI) pages. It is enhanced to split the information (based on the European Payments Council (EPC) guideline), when there are more than 280 characters (inclusive of business and service content). This populates the additional characters in subsequent structured remittance information occurrences while sending an outgoing message to clearing.

SEPA CT PI version pages (in `PO` and OE) perform certain validations based on the occurrences, before accepting the payments initiated by the user.

[Bulking Criteria for Equens CT](#)

The outgoing SEPA Equens CT payments are clubbed based on the interbank settlement date. Different files are generated for different interbank dates. However, different payment types cannot be clubbed into single file. For example, pacs.008, pacs.004, pacs.028, camt.029, camt.027, camt.087 and camt.056 cannot be clubbed into the same file.

[Retrieving Original Credit Transfer](#)

During an incoming return, when a camt.056 or camt.029 message is received, the original credit transfer message is retrieved based on the following conditions:

- Transaction amount
- Settlement date
- Original transaction ID in the R-transaction against transaction ID (original payment)

[Handling PSR (pacs.002s2)](#)

The pacs.002s2 clearing status report for the SCT messages sent to clearing (pacs.008, pacs.004, camt.056, camt.029, camt.027, camt.087 and camt.029(v8.0)) is sent to the originator bank. The payment clearing status report (pacs.002s2) can be classified into three types of acceptance and rejection:

| Level | Description |
| --- | --- |
| File level | Can be a complete file acceptance or rejection. |
| Bulk level | Denotes the bulk-level acceptance or rejection of the outward credit transfer message sent to the clearing.  - Some bulks are fully accepted or rejected - Some payments within the file are accepted while others are rejected. |
| Transaction level | Provides information on the number of transactions accepted and rejected inside the bulk. Payment information details are provided for the rejected transactions. |

The clearing status report received can be a processed STP or Non-STP. It is parked for manual action based on the reason code in the incoming pacs.002s2 (this is done by configuring the *Route To Exception* field to Yes). The user can take manual actions, such as resubmit, reject or return the transaction from the Sent Exception page. The user can resubmit or reinitiate the clearing of rejected camt.027, camt.087 or camt.029 (v8.0) message from the enquiry again.

[Receiving Clearing Status Report (pacs.002s2) and Forwarding to Indirect Participant Bank](#)

When a pacs.002S2 reject message is received for an outgoing pacs.008 , pacs.004, camt.056 (cancellation request) and camt.029 (resolution of investigation) originated from IP (based on the parameterisation in TPH), it moves the rejected transactions to the Sent Exception page for manual intervention. This enables the bank users to perform the following actions:

| Action | Description |
| --- | --- |
| Resubmit | The user performs the following actions:  - Cannot resubmit the   camt.056 or camt.029 message to the clearing, as it displays an error message - Can resubmit the   pacs.008 or pacs.004 message to the clearing |
| Return or Reverse | The Clearing performs the following:  - Rejected pacs.004, camt.056 or camt.029   is forwarded as pacs.002s2 to the IP - Rejected pacs.008 is sent as pacs.004 to the   IP |

[Indirect Participation in SEPA](#)

- TPH as an indirect participant bank can be configured to initiate or receive SEPA payments.
- TPH as a direct participant bank can receive and send SEPA payments from an indirect participant bank or route it to clearing (EBA).

[Enquiries to View the Sent or Received CT File](#)

TPH has the enquiries to view all the Direct Debit (DD) or Credit Transfer (CT) files received from IP or Clearing channel. The user can navigate to the bulk level enquiry from the file level enquiry and further transaction level enquiry.

[Enquiry to View Unmatched R-Messages](#)

- To list the CT return transactions (pacs.004) in repair status (status code - 235) with ‘Original Transaction is Not Found Error’ or ‘Transaction Not in Completed' status, go to **Payment Inquiries**>**Pending Payments**>**Pending Unmatched R-Payments Enquiry**.
- Enter the FT number of original transaction in the *Original Transaction Reference* field, when releasing the payment from general repair queue or new inquiry.

- This field is mapped to *OriginalorReturnId* field in `POR.Supplementary.Info` table.
- TPH validates whether the entered FT number exists in the system and is in 'Completed' status.
- Additionally, allows to release the transaction from repair without entering the original transaction reference (when original transaction is not migrated from legacy system to TPH).

[Outward Processing of SEPA CT (pacs.008) Initiation](#)

This section describes the outward processing of a SEPA SCT payment initiated in TPH bank, or initiation request received from customer in the form of pain.001 message.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA credit transfer payment from branch or back office by using `PAYMENT.ORDER` (`PO`) application or OE page | Captures an SCT payment from `PO` application or TPH OE page. Validates mandatory and non-mandatory fields on submission and displays error (if any). |
| Payment initiation using pain.001 message | Initiates an SCT by sending a pain.001 message to the ordering bank. |
| Account validations | Validates the following for the ordering account:  - Is a valid Temenos Transact account - Has no posting restrictions - Has sufficient balance to cover the transaction |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly or indirectly (if configured) |
| Balance check (not shown in diagram) | Checks whether the debit account has enough funds for the payment to be processed. If available, it reserves the funds. |
| Submission and Supervisor approval | Performs the following validation:  - On submission of payment, it waits for Supervisor’s approval.  - Once approved, it is moved for further processing. - If rejected, it is modified and resubmitted for approval.  - It is then sent to Temenos Payments Hub Engine for further processing. - Payments received in TPH from external banks in STP mode do not wait for Supervisor’s approval. |
| Warehouse | Warehouses payments with future execution date and releases on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement, which is performed in the site.  TPH solution is pre-integrated with Temenos Financial Crime Mitigation (FCM) solution. |
| Routing | Routes the payment to a TPH clearing channel (STEP2), which is configured to route to SEPA payment.   Clearing channel determines the message type (pacs.008). |
| Dates calculation | Calculates the payment value and booking dates, which is configured to current date (similar to the execution date) |
| FX calculation | Applies when customer account and payment account currencies are different. If FX shifts are involved, it adjusts value date forward and warehouses the payment.   This feature is supported with Payments Hub (PH) license. |
| Balance reservation | Reserves funds on the debit account. It is done on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. |
| Duplicate check | Performs duplicate check on payments received from ordering or indirect participant bank for a set of payment attributes, such as payment amount, currency and transaction reference |
| Posting | Debits the payment amount and any charges to be borne by the customer to the debtor account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (automatic retry, reject or cancel).  - If Account Management System (AMS) is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward payments are entries made before sending pacs.008 to Clearing.  - Child transaction entries  - Debit debtor account (or ordering bank account) - Credit suspense account  - Settlement transaction entries (bulk)  - Debit suspense account  - Credit EBA clearing Nostro account |
| SEPA channel validations | Ensures the payment meets the compliance requirements of SEPA. |
| Outward payment generation | Generates pacs.008 message. |
| Error queue | If an error occurs while processing SEPA payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

[Inward Processing of Equens SEPA Credit Transfer (pacs.008) Request](#)

This section describes the inward processing of a payment received from clearing in TPH account or another bank (indirect participant).



| Activity | Description |
| --- | --- |
| SCT payment received from clearing network | Receives an inward payment pacs.008 from clearing in TPH. |
| SEPA specific format validations | Performs SEPA specific validations on the payment. |
| Account validation | Validates the beneficiary account for the following:  - Number is invalid - Closed - Stopped |
| Dates calculation | Receives SEPA payments with value date configured as current business date. Payment is processed immediately. |
| Filtering | Performs filtering of payments (if configured). This is a bank-specific requirement, which is performed in the site. |
| Fee calculation | Debits charge associated with payment from the customer account. |
| Duplicate check | Performs duplicate check on payments received from SEPA for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | Raises the following accounting entries for an incoming pacs.008:  - Settlement entry (bulk)  - Debit clearing Nostro - Credit suspense account  - Child transaction  - Debit suspense account - Credit customer account |
| Payment archived or redirected to indirect participant | Routes the payment to the IP bank (when the incoming pacs.008 final beneficiary is an IP) or marks it as completed. |
| Error queue | If an errors occurs while processing a SEPA payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

## File Naming Convention for Equens SEPA CT

The outward file name generated for Equens SEPA CT message has the following components:

- Sender
- Destination
- File type
- Reference
- Extension

An outgoing file sent to clearing (CT payment instruction) is **xxxxxxxx.SFT.CTPI.yyyyyyyy.XML**.

Where,

- SFT is Secure File Transfer when EquensWorldline is receiving the files
- 'xxxxxxxx' is the customer address
- 'yyyyyyyy' is the unique reference number generated by the system. The customer address (for example, R5700011) is mapped from the clearing table

The following are the outgoing messages:

| Credit Transfer Messages | Flow Direction | File Type |
| --- | --- | --- |
| CT payment instruction, pacs.008.001.02 | Bank-EquensWorldline | CTPI |
| CT return, pacs.004.001.02 | Bank-EquensWorldline | CTRT |
| CT recall from bank (camt.056.001.01) | Bank-EquensWorldline | CTRFB |
| CT recall negative answer from bank (camt.029.001.03) | Bank-EquensWorldline | CTRNFB |
| CT status request from bank (on camt.056/027/087) (pacs.028.001.01) | Bank-EquensWorldline | CTSRFB |
| CT claim non-receipt from bank (camt.027.001.06) | Bank-EquensWorldline | CTCNFB |
| CT claim for value date correction from bank (camt.087.001.05) | Bank-EquensWorldline | CTCVFB |
| CT for inquiry response from bank (Camt.029.001.08) | Bank-EquensWorldline | CTCRFB |

## Equens SEPA 2021 Credit Transfer Rule Book Changes

The following functionalities are provided to cover the SEPA 2021 Rule Book updates for Equens CT and DD:

- Receive and process a bank request with a specific reason code, within the acceptance days configured for that reason code.
- The Additional Information tag has been made mandatory from optional, maximum 13 occurrences are allowed.
- Initiate and process a fee and interest compensation payment via a credit transfer request (pacs.008.001.02). A pacs.008 has been added for a payment of inter-PSP fee and/or interest compensation related to the inquiry messages camt.027/087.
- An enquiry on multiple credit transfer transactions is allowed.
- It possible to request only a fee (in charges) without necessarily an interest compensation (in compensation).
- Link Equens payments with preceding request-to-pay. RRTP is used in case the SCT is the result of a preceding request-to-pay message (RTP). EquensWorldline will accept and forward this code.
- The reject codes XT74 and XT75 are replaced with AG09 and RCON for both SCT and SDD.

## Equens SEPA 2023 Credit Transfer Rule Book Changes

This functionality allows banks to support the Equens SCT clearing functionality with the latest up to date rulebook changes published for 2023, respectively enhancing the outward and inward for the below messages.

| Messages | Transaction Type |
| --- | --- |
| pacs.008 | Credit Transfer |
| pacs.002 | Clearing status report |
| camt.056 | Cancellation Request |
| camt.029 | Resolution of Investigation |
| pacs.004 | Return Credit Transfer |
| pacs.028 | Status Request |
| camt.027 | Claim of Non-Receipt |
| camt.087 | Claim for Value date correction |

The Equens RB change enables the migrating to the 2019 version of the ISO 20022 and thus, offers the end user the opportunity of using the features under the 2019 version which may not be available under the earlier versions of the ISO 20022 standard.

- The existing version of the message identifiers is changed to a newer version, therefore, even the xsd will be replaced with the newer version in order to support the latest changes.

  | Message older version | Message new version |
  | --- | --- |
  | pacs.008.001.02 | pacs.008.001.08 |
  | pacs.002.001.03 | pacs.002.001.10 |
  | camt.056.001.01 | camt.056.001.08 |
  | camt.029.001.03 | camt.029.001.09 |
  | pacs.004.001.02 | pacs.004.001.09 |
  | pacs.028.001.01 | pacs.028.001.03 |
  | camt.027.001.06 | camt.027.001.07 |
  | camt.087.001.05 | camt.087.001.06 |
- The reference *Id*'s can now contain internal spaces, however leading/trailing spaces are not allowed.
- The element “BIC” (2009 message version) is changed to “BICFI” (2019 message version) and the element “BICOrBEI” (2009 message version) is changed to “AnyBIC” (2019 message version).
- LEI is a new sub-element introduced under the organisation identification for debtor, creditor, ultimate debtor and ultimate creditor. When organisation identification is used either AnyBIC, LEI or One occurrence of Other must be present. Its is a 20-digit alphanumeric characters value.
- After the RB change 2023 payment end-users can benefit from the standard delivery of structured address details about the payer and the payee. It consists of the Country and TownName (both mandatory) together with one or more of the other structured elements Department, SubDepartment, StreetName, BuildingNumber, BuildingName, Floor, PostBox, Room, PostCode, TownLocationName, DistrictName and CountrySubDivision. The user has the option to capture either the Structured or Unstructured address. The current unstructured PostalAddress can be used in combination with country.
- Proxy is a new sub element (optional) under the Debtor Account and Creditor Account tag. It is optional, it can be used in addition to the (mandatory) IBAN, it doesn’t replace the IBAN. When used proxy identification is mandatory and character limit cannot exceed 320 alphanumeric in length.
- Creditor reference information can be used to capture the remittance information and when used then the structure type, structure issuer and structure reference is mandatory.
- Original message name identification in the R messages now will contain the complete version of the original underlying message.
- The proprietary reasons codes TECH, FRAD, AC03 and AM09 in camt.056 and the proprietary codes AC04, AM04, NOAS, NOOR and ARDT in camt.029 are now moved under the reason codes and usage of the additional information now should be based on the allowed reason under the ISO reason codes.
- Element Purpose is now present in the R messages and value must be present if it was present in the original message.
- New sub element party is introduced for all the party role tags - Debtor, Creditor, Ultimate Debtor, Ultimate Creditor. For example: Dbtr\_Nm changed to Dbtr\_Pty\_Nm.
- The element Charges Information sub-element Party is replaced by Agent. As a result, in the pacs.004 Positive Response to Recall ChrgsInf\_Pty\_FinInstnId\_BIC changed to ChrgsInf\_Agt\_FinInstnId\_BICFI.

## Equens SCT Rulebook changes for 2025

The Equens Credit Transfer (CT) clearing solution is fully compliant with the 2025 SEPA rulebook changes. Following are the key updates for Credit Transfers, which are applicable for the pacs.008, pacs.004, camt.056, camt.087, camt.027, and pacs.028 message types:

- **Ultimate Debtor and Debtor<Org ID>**: For the SCT message types, the Organisation Identification sub-element under Ultimate Debtor and Debtor must include any BIC, LEI, and may contain one occurrence of ‘Other’.
- **Hybrid Postal Address Support**: Debtor and Creditor elements support Hybrid Postal Address. Town and Country are mandatory, and at least one address line is supported.
- **Clearing Directory File Format**: The Clearing Directory File Upload process supports the new reach file format (rocs.001.001.07).

In this topic

- [Introduction to Equens SEPA Credit Transfer](#IntroductiontoEquensSEPACreditTransfer)

- [File Naming Convention for Equens SEPA CT](#FileNamingConventionforEquensSEPACT)
- [Equens SEPA 2021 Credit Transfer Rule Book Changes](#EquensSEPA2021CreditTransferRuleBookChanges)
- [Equens SEPA 2023 Credit Transfer Rule Book Changes](#EquensSEPA2023CreditTransferRuleBookChanges)
- [Equens SCT Rulebook changes for 2025](#EquensSCTRulebookchangesfor2025)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:34 PM IST