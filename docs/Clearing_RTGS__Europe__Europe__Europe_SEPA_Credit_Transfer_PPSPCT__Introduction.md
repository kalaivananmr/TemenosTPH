# Introduction to SEPA Credit Transfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
  - [SEPA Credit Transfer SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
    - [Introduction](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
    - [Configuration](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Configuration.htm)
    - [Working with](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Working_with.htm)
    - [Tasks](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Tasks.htm)
    - [Outputs](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Outputs.htm)
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

# Introduction to SEPA Credit Transfer

Updated On 27 March 2026 |
 52 Min(s) read

Feedback
Summarize

The Single Euro Payments Area (SEPA) is an initiative to create a zone for the Euro, where:

- All electronic payments are considered domestic.
- Difference between national and Intra-European cross-border payments does not exist.

The project aims to improve the efficiency of cross-border payments and convert the fragmented national markets for Euro payments to single domestic. It enables the customer to make cashless Euro payments to any person located anywhere by using a single bank account and single set of payment instruments. SEPA Credit Transfer (SCT) allows transfer of funds from one bank account to another. SEPA clearing rules require the payments that are made before the cut-off point on a working day, hence, it can be credited to the recipients account within one working day. SEPA CT comply to Wire Transfer Regulation (WTR).

SEPA Credit Transfer (STEP2) module in Temenos Payments Hub is compliant to ‘STEP2 – SEPA Credit Transfer Bulk and Batch Processing Service 2025’.

[Types of Participants](#)

There are two type of participants in SCT payments:

| Type of Participant | Description |
| --- | --- |
| Direct Member | A participant bank that exchanges payments directly to the clearing (EBA, Equens, RPSSCL) and holds a settlement account with clearing. |
| Indirect Member | A member bank that exchanges payments with clearing through SEPA direct member and does not hold a settlement account with SEPA clearing. |

TPH can be configured to act as SEPA direct participant that directly interacts with SEPA clearing house or as indirect participant to send payment messages to direct participant bank.

[](#)[Types of Payment and Messages](#)

SEPA Credit Transfer bulks and processes the messages in several files. TPH supports the following files and message types:

| File Type | Name | Description |
| --- | --- | --- |
| ICF | Input Credit File | The direct participant’s systems use this file to transmit transactions to the central system |
| CVF | Credit Validation File | Defines the success or otherwise of the validation process. The central system returns this file, per transmitted ICF, to the sending direct participant |
| SCF | Settled Credit File | Delivers settled transaction to the relevant counterparty |
| CCF | Cancelled Credit File | CSM clearing sends the cancellation payment status report to the originating bank if the credit transfer request (including returns) gets cancelled at the CSM (due to settlement failure, or inability to be rolled over to any settlement cycle for the business date). Additional CCF files are generated upon activation of the relevant parameter (for those participants that opted for this configuration). It reports any transaction cancelled during the settlement process and automatically resubmits to the next available settlement cycle |
| LNR | Liquidity Notification Report | STEP2-CGS notifies the direct participants whenever a threshold is exceeded in its liquidity position or when a liquidity adjustment is executed |
| PCF | Payment Cancellation File | CSM clearing sends this payment cancellation request status to the originating bank indicating the status of the cancellation request (cancelled at the clearing or forwarded to the beneficiary bank as a recall). This report is generated based on agreement with the originating bank |

TPH supports the following SCT message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.08 | B2B | Customer credit transfer | Inward and outward |
| pacs.004.001.09 | B2B | Return | Inward and outward |
| camt.056.001.08 | B2B | Payment cancellation request or request for recall | Inward and outward |
| camt.029.001.09 | B2B | Resolution of investigation | Inward and outward |
| pacs.028.001.03 | B2B | Request for status update | TPH supports the following:   - Inward and Outward - Receive the Request for Status Update   - From Clearing and forward to IP   - From IP and forward to Clearing or another IP |
| pacs.002.001.10S2 | B2B | Clearing payment status report | Inward |
| pain.001.001.03 | C2B | Credit transfer initiation | Inward |
| pain.001.001.02 | C2B | Credit transfer initiation | Inward |
| pain.001.001.09 | C2PSP | Credit transfer initiation | Inward |
| pain.002.001.03 | B2C | Payment status report to customer | Outward |
| pain.002.001.02 | B2C | Payment status report to customer | Outward |
| pain.002.001.10 | PSP2C | Payment status report to customer | Outward |
| pain.001.001.05 | C2B | Credit transfer initiation | Inward |
| camt.087.001.06 | B2B | Request to modify value date | TPH supports the following:   - Inward and outward - Receives the Request to Modify Value Date message,   - From Clearing and forward to IP   - From IP and forward to Clearing or another IP |
| camt.027.001.07 | B2B | Claim non-receipt | Inward and outward |
| camt.029.001.09 | B2B | Resolution of investigation | TPH supports the following:   - Inward and outward - Receives the Responses for Investigation message   - From Clearing and forward to IP   - From IP and forward to Clearing or another IP |
| camt.054.001.10 | B2B | Liquidity Notification Report | Inward |

[Payment Instruments](#)

SEPA payment instrument is SCT.

[Bank Identifier Code (BIC) and IBAN](#)

The preferred bank or branch and beneficiary account identification methods used in SEPA are IBAN and BICs, respectively. As a part of SEPA regulation, SCT payment (pain.001) initiated by the customer can come without the beneficiary BIC. The beneficiary BIC is derived from the beneficiary IBAN.

In addition to the IBAN, the user can also initiate a SEPA payment with the debtor and creditor proxy identification, which serves as an additional information for the debtor and creditor.

[Initiating Customer Credit Transfers](#)

SCT can be initiated using the following:

|  |  |
| --- | --- |
| pain001 | System supports both single and bulk pain.001. It can result in book (beneficiary in the books of the processing bank) or outward transfer (pacs.008 is sent to clearing). |
| Payment Order | - User needs to input ordering and beneficiary customer details, payment amount, payment currency, requested execution date or requested credit value date calculated based on payment order product configuration, which is validated and committed. - Authoriser approves the payment order, and the system processes it as a book or an outward payment depending on where the beneficiary resides. The pacs.008 message is sent to clearing for outward payments.   If the originating source of payment from the PO application is Request To Pay (RTP), then it populates the *Purpose* field with RRTP in outgoing SEPA transaction (pacs.008). This links the Request To Pay payment with subsequent SEPA Credit Transfer Payment. |
| Order Entry (OE) | - User needs to input ordering and beneficiary customer details, payment amount, payment currency and debit value date in the OE page, which is validated and committed. - Authoriser approves the payment order and system processes it as a book or an outward payment depending on the residency of the beneficiary. The pacs.008 SCT reachability is sent for outward payments. |

OE or PO screens are used for customer credit transfers related to fee, charge, or interest payment that are the results of enquiry, such as camt.027 or camt.087.

SEPA clearing house provides the SEPA routing directory file and uploads it to the `CA.CLEARING.DIRECTORY` table in TPH. System decides whether the beneficiary BIC is reachable based on the following conditions:

- Belongs to the SCT scheme.
- Status of the participant as ‘Enabled’.
- Start date indicates the date from which the BIC becomes active and can be used in SEPA payments.
- End date indicates the date after which the BIC cannot participate in SEPA payments.

[SEPA CT Cut-Off Time](#)

The SCT payments can be sent to the clearing, three days prior to the requested credit value date. Hence, clearing does not accept any SCT payment that is received before this time period.

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

[Returning SCT (pacs.004)](#)

The beneficiary bank can return SCT when it cannot process the payment. For example, invalid creditor IBAN, credit account is closed, posting restrictions on the creditor account, and so on. It can be returned automatically or manually based on the following configuration:

- If a return payment is initiated, TPH reverses the original payment booking and moves it to the Payment Completed with Return (996) business state. It creates and sends a new return payment to clearing, which ensures to credit the Clearing Nostro.
- If a return payment is received, it processes and books the received return payment (when the original payment for the return exists). In this case, the customer who is debited (initially) gets credited. It updates the original credit transfer to Payment Completed with Return (996) business state.
- If a return payment for the redirected transaction from STEP2 is received, TPH matches the return payment with original transaction and determines the output channel based on R&S. TPH performs the channel validation for the return transaction before sending it out.

[Recalling a Settled Credit Transfer (camt.056)](#)

SCT sent to clearing (by the originator bank) can be recalled by sending a camt.056 (cancellation) recall request message (initiated by the originator or originator bank of the credit transfer). TPH can initiate a cancellation request and specify whether it is initiated by the customer or bank. The system automatically defaults the number of values from the original payment to the cancellation request and the user updates a reason code stating the reason for cancellation. No accounting entries are raised for this message as it is a non-financial message. If TPH is the beneficiary bank receiving the camt.056 recall request, then it can respond with a positive answer by sending a pacs.004 return message. Return payment (pacs.004) is initiated by the following:

- Creating new return transaction
- Debiting a customer account (which was earlier credited by the incoming credit transfer)
- Creating settlement entries to credit the clearing Nostro.

The status of the original credit transfer is updated as Payment Completed with Return (996) business state. The beneficiary bank can respond with a negative response (by sending a camt.029 Resolution of Investigation (ROI) message) indicating the rejection of recall request received from the originator bank. It is a non-financial message that:

- Has no accounting entries raised during the process.
- Is initiated when the reason code for rejection is entered.

The response to an incoming cancellation request can be initiated manually or automatically. When the beneficiary bank receives the recall request, it retrieves the original credit transfer payment for which the recall has been received.

- If the original transaction is not found, the cancellation request is rejected automatically based on the configuration.
- If the original credit transfer details are retrieved, the system checks whether the cancellation request can be processed automatically based on the configuration.

[ Example](#)

- If the *AutoReturnIndicator* flag is set to N, it parks the cancellation request for manual action.
- If not, it processes the cancellation request automatically to return the original credit transfer by using pacs.004.

- If a customer initiates a cancellation request, the system checks whether it is within the acceptance days. Otherwise, it is rejected by sending camt.029 message.

If it is within the acceptance days, the return processing of the original credit transfer is done either manually or automatically based on configuration.

- The acceptance day’s check to initiate a cancellation request can be configured separately for customer and bank initiated recall requests.

TPH will allow user to initiate only one recall for an underlying SEPA Credit Transfer even if initial recall is unanswered or negative response received for initial recall.

The debtor can set a period to avail a refund depending on the authorisation or unauthorisation of DD mandate.

[Initiating a Bulk Recall Request (camt.056)](#)

TPH can initiate a bulk cancellation request by selecting multiple credit transfers. If the reason code for the cancellation request is provided and bulk cancellation request is authorised, the camt.056 message is generated.

[Requesting for Status Update (pacs.028)](#)

This message (non-financial) is sent to enquire the status of the 'Cancellation Request' (camt.056). The originator bank can initiate this request from the enquiry provided. When the beneficiary bank receives a request for status update (pacs.028), it performs the following:

- If the recall request is already accepted (that is, a return payment is sent to the originator bank), it generates a camt.029 (negative response) with 'ADRT' status as a response.
- If the recall request is already rejected (that is, a camt.029 is sent to the originator bank), it generates a camt.029 (negative response) with the original reject reason code as a response.

If the bank receives multiple investigation requests in an incoming file, TPH de-bulks and processes it.

The ordering bank can send a request for status update (pacs.028) for camt.27 and camt.87, and the beneficiary bank can receive and process it. Additionally, it can send a request to the beneficiary bank for status update of an inquiry for which they have not received any response.

| Status Update | Description |
| --- | --- |
| Outgoing Request | Provides the user with an enquiry to initiate a status update request (pacs.028) for an outgoing camt.027 or camt.087. |
| Incoming Request | When an incoming request for status update is received, the system checks for camt.027 or camt.087 request from the originator bank.   - If a matching record is not available, the system updates the status to 'Unmatched'. - If a matching record is found, the system checks whether camt.029 response is sent as a response for the incoming camt.027 or camt.087.   - If camt.029 response is sent already, the user does not send it again.   - If camt.029 response is not sent, the user can initiate     the response (manually) from the enquiry. |
| Incoming Request (redirected for IP) | When an incoming Request for Status Update is received, the system checks for the underlying Cancellation Request (camt.056), Claim of Non-Receipt (camt.027), or Request To Modify Value Date (camt.087) messages from the originator bank.   - If a matching record is available and the beneficiary is not in the books of the processing bank, the system forwards the Request to Status Update to IP or Clearing. - If a matching record is available, the system checks whether the response (camt.029) is already sent for the incoming enquiry (camt.56, camt.027, or camt.087).   - If camt.029 response is already sent, the user does not send it again.   - If camt.029 response is not sent, the user can manually initiate the response from the original enquiry such as, camt.056, camt.027, or camt.087.  - If a matching record is not available, the system updates the status to 'Unmatched'. |

[Claiming for Non-Receipt by Originator (camt.027)](#)

A new message type is introduced as part of SEPA 2019 changes for the originator or beneficiary of the payment to send or receive a claim of non-receipt of initial credit transfer. This is performed when the beneficiary claiming non-receipt contacts the user.

| Message Type | Description |
| --- | --- |
| Outgoing camt.027 | Provides the user with an enquiry to initiate a camt.027. This enquiry lists all the outgoing pacs.008 in 'Completed' status, which are sent to clearing.   - When initiating the   camt.027 from the enquiry, the system checks for request that is initiated   within 13 months of the original credit transfer.   - If     initiated outside the parameterised time frame, it displays an error message and     does not allow the user to initiate the camt.027 request. |
| Incoming camt.027 | - Processes and uploads the incoming camt.027 message - Provides the enquiry to the user to view the incoming camt.027 message - System matches the incoming camt.027 with the original pacs.008, which is already processed.   - If the original payment is found and is in a completed state, the system automatically (configuration) generates camt.029 with status code as ACNR. Also, places the acceptance date of the camt.027 claim and maps the process in the outgoing camt.029.   - If the original payment is found and is in 'Cancelled, Rejected and Returned' status, the system automatically generates (configuration) camt.029 with status code as RJNR and reason code as ARDT in the outgoing camt.029.   - If the original payment is not found, the system automatically rejects the camt.029 with reason code as NOOR and status as 'RJNR'.   - If the original payment is not found and the system is configured for manual action, it parks the camt.027 to Unmatched queue for manual action.   The user needs to perform the following, when camt.027 is parked for manual action:  - Initiate the Resolution of Investigation - camt.029 message from the enquiry in response to an incoming claim of Non-Receipt - camt.027. - Perform additional   check whether the incoming camt.027 is responded by the beneficiary bank within 10 days of the receipt of the camt.027 message. - Claim charges for handling the enquiry. The following values are available in the outgoing cam.029 only when the selected status code is ACNR   - Charge amount   - Charges BIC   - Charges IBAN - Map and bulk the outgoing camt.029, and generate the file in the output folder. |

[Claiming for Value Date Correction or Requesting to Modify Payment (camt.087)](#)

A new message type introduced as part of SEPA 2019 changes for the originator or beneficiary of the payment to send or receive a value date confirmation or modification request of initial credit transfer. This is performed when the beneficiary (claiming non-receipt of funds) contacts on the intended value date. The incoming camt.087 message indicates a modification in the payment due to change in the interbank settlement date.

| Message Type | Description |
| --- | --- |
| Outgoing camt.087 | Provides the user with an enquiry to initiate a camt.087. The enquiry lists all the outgoing pacs.008 in 'Completed' status, which are sent to clearing.   - When initiating the   camt.087 from the enquiry, the system checks whether the request is initiated   within 13 months of the original credit transfer.   - If initiated outside the parameterised timeframe, it     displays an error message and does not allow the user to initiate the     camt.087.    The   modified *Interbank Settlement Date* field   is defaulted with original credit value date of outgoing pacs.008.   - If there is no change in the modified interbank     settlement date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become mandatory.   - If the user changes the date in modified *Interbank Settlement* field to a new     date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become     non-mandatory.   Updates the status of camt.087 to 'Claim Sent' status in TPH. Additionally, it bulks the outgoing camt.027 and generates it in the outgoing message folder. |
| Incoming camt.087 | The system performs the following when the beneficiary bank receives a camt.087 message:   - Processes and uploads the incoming camt.087 message. - Provides the enquiry to the user to view the incoming camt.087 message. - Matches the incoming camt.087 with the original pacs.008, which are already processed   - If the original payment is not found, the system updates the status to 'Unmatched'.   - If the original payment is found, the system checks whether camt.087 is received within the acceptance days.    - If yes, it proceeds with Straight-Through Processing (STP) of the camt.087 message   - If not, it parks the incoming camt.087 for manual intervention   - If the original payment is found and is within acceptance days, system checks whether the original payment is in 'Completed' status.    - If yes, it proceeds with STP of the camt.087 message   - If not, it updates the incoming camt.087 status as invalid claim. The claim is invalid as the original payment is returned already and does not allow to modify the date in the original payment. Hence, the user cannot perform any manual action as the claim is set as Invalid.   - If the original payment is in 'Completed' status and *Automated Return Indicator* is set to Yes, the system checks whether the modified and original credit value date of pacs.008 transaction is same.    - If the dates are not same, it parks the camt.087 request for manual action and updates the status to 'Inwork'.   - If the dates are same, it automatically generates the camt.029 with status as 'RJVA'.   User can select one of the following option when an inward camt.087 is parked for manual action. The value of status field in response ROI is determined on basis of this selection.   - **Accepted value date adjustment (ACVA)** - This is a ‘confirmed positive’ response provided by Beneficiary PSP to indicate that an inward ‘Claim for Value date correction’ request has been accepted.   - User can respond to an inward Claim (camt.087) with a Resolution of Investigation message (ROI) in camt.029 format from ‘Inward Requests Require Manual Action’ enquiry. Read the Working with topic for more information.   - System will allow user to provide fee and / or compensation details manually when status of outward ROI is ACVA. This information is mapped to the outgoing camt.029 message and no accounting entries will be raised for the charges or compensation amount.   - No correction entry or reversal posting is generated in TPH when ACVA response is generated   - Such inquiries/ cases will be on-hold until payment for interest compensation or charges is received from Originator PSP   - Upon receipt of interest payment/ charges, system will reverse the original payment and create a new payment with the new value date as requested by the originating bank. A second ‘Resolution of Investigation’ (camt.029) is generated with the status code as MODI to confirm to originator that value date modification is completed successfully. - **Modified as per request (MODI)** - In this response, ROI indicates that beneficiary PSP has modified the value date of the original transaction based on request from the originator bank. Beneficiary PSP can initiate a MODI response in following scenarios:   1. As first response to an inward camt.087 – when system is able to determine the underlying inward CT and the same is in completed status. User can populate Fee & Or compensation amount (optional).   2. As second response to an inward camt.087 – when beneficiary PSP has sent ACVA as initial response, received fee and/ or interest compensation interest payment and modified the value date as per the inward claim.   User can initiate a Resolution of Investigation message (first or second ROI) to an inward ‘Claim for value date modification’ (camt.087) from ‘Inward Requests Require Manual Action’ enquiry. Read the [Working with](Working_with.htm) topic for more information.  TPH allows the user to initiate second ROI with status as MODI when there is no response to the first response with status ACVA. The user can provide the fee and/or interest compensation details manually in such response.  When MODI response is generated, original payment is reversed and a new payment is created with the value date as requested by the originating PSP in inward ‘Claim for value date modification’ (camt.087). |
| Incoming camt.087 (Redirected to IP or Clearing) | The system performs the following when the beneficiary bank receives a camt.087 message:   - Processes and uploads the incoming Request to Modify Value Date (camt.087) message - Provides the enquiry to the user to view the incoming Request to Modify Value Date (camt.087) message - The system matches the incoming camt.087 with the original pacs.008, which is already processed or cancelled and the direction is ‘R – Redirected’. - If the system finds the original payment and the payment is in Completed state, the system automatically forwards the camt.087 message to the Indirect Participant (IP) based on the *AutomatedReturnIndicator* field configured in the `PP.CLEARING.SETTING` table. - If the system finds the original payment and the payment is in Rejected, Returned, or fund-seized status, the system automatically generates camt.029 with status code as CVAA or RJVA based on the *AutomatedReturnIndicator* field configured in the `PP.CLEARING.SETTING` table. - If the original payment is not found, the system automatically rejects the camt.029 message with reason code as NOOR and status as RJVA or CVAA. - If the original payment is not found and the system is configured for manual action, it parks the camt.087 to the unmatched queue for manual action.   When the system parks camt.087 for manual action, the user needs to perform the following steps:   - Initiate the Resolution of Investigation - camt.029 response message from the enquiry in response to an incoming Request to Modify Value Date (camt.087), where the status of the original payment is in Rejected, Returned, or fund-seized. - If the original payment is already processed or cancelled and direction is R – Redirected, forward the Request to Modify Value Date (camt.087) message to Clearing or IP. |
| Response to Redirected Enquiry | TPH (beneficiary bank) receive the Response-to-SCT-Inquiry message (camt.029) and forward the same to Clearing or IP.   - If the system have processed the original Request to Modify Value Date message and forwarded to IP or Clearing, the response camt.029 is sent (automatically or manually) to originator bank that requested the enquiry. - If the system receives the response camt.029 from IP or Clearing twice, that is if the system receives camt.029 with ACVA follows by MODI status, TPH forward both responses to Clearing or IP. |

[](#)[Supporting Structured and Hybrid address](#)

The participant bank users can also initiate a SEPA payment by providing hybrid address specifically structured address details and atleast one occurrence of address line. The user can input hybrid address or structured address details or unstructured address lines. If structured address lines are used, the SEPA payment expects a value for at least *Town Name* and *Country*.

The PAYMENT.ORDER application, **Order Entry** screen, and pain.001 supports the initiation of SEPA payments using structured address details and hybrid address.

The following screen shots display the initiation of SEPA payments in the PAYMENT.ORDER application and **Order Entry** screen.



[Supporting Extended Remittance Information](#)

When a pain.001 file is received with both structured and unstructured information, the details are stored in the TPH table. According to the rulebook, the local instrument code is available with PERI. The system checks the beneficiary bank BIC that supports ERI payment option (based on which the structured and unstructured information are mapped in the outgoing pacs.008 message) before generating the pacs.008 message to clearing. TPH system performs validation to update the local instrument code PERI received in the pain.001 file in the respective TPH table. The reachability API checks whether the beneficiary bank supports ERI option based on the information from the STEP2 routing table. During validation, it checks for the total character length of 280 characters for structured tags in ERI payment option.

- If the incoming pain.001 does not have the local instrument code as PERI, it updates in the TPH table based on reachability API check.
- If the API return the value ERI, it updates the local instrument code as PERI in TPH.

| Scenario | Tag |
| --- | --- |
| Outward pacs.008 Mapping | |
| Local Instrument Code is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code is equal to PERI | Maps max 999 occurrences with all structured remittance tags |
| Outward R-messages Mapping (pacs.004, pacs.028, camt.056, camt.029, camt.029, camt.027, camt.087) | |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is equal to PERI | Does not map any remittance information |

While initiating and sending outgoing camt.056, pacs.004, camt.029 and pacs.028, the system checks the original payment (pacs.008) for the local instrument code.

- If it has PERI, the structured information is not sent in the outgoing camt.056, pacs.004, camt.029, camt.027, camt.087 and pacs.028.

While receiving pacs.008 message from clearing, it maps the local instrument code PERI to the respective TPH table and stores the structured remittance information in the remittance information table in TPH.

[](#)[`PP.ORDER.ENTRY` (OE) and `PAYMENT.ORDER` (PO) Application](#)

Extended Remittance Information (ERI) allows participant bank users in entering details (upto 999 occurrences) of structured remittance information when initiating CT from Payment Initiation (PI) pages. It is enhanced to split the information (based on the European Payments Council (EPC) guideline), when there are more than 280 characters (inclusive of business and service content). This populates the additional characters in subsequent structured remittance information occurrences while sending an outgoing message to clearing.

SEPA CT PI version pages (in PO and OE) perform certain validations based on the occurrences, before accepting the payments initiated by the user.

[Bulking Criteria](#)

A file sent to SEPA is an Input Credit File (ICF). The outgoing file can have multiple bulks with multiple transactions. It can have pacs.008, pacs.004, camt.056 and camt.029 bulked in one file. Different message types (for example, pacs.008 and pacs.004) cannot be bulked in the same bulk. It is bulked as two separate bulks in the same file. The bulking criteria for SEPA files are as follows:

- Transaction currency
- Clearing nature code
- Message type (pacs.008, pac.004 and so on)
- Clearing transaction type (CT, RT)
- Credit value date

The bulking logic given above is applicable for both STEP2 and RPSSCL. In case of fee related payment, where the category purpose code in FCOL (Fee Collection), INTE (Interest) or FCIN (Fee Collection and Interest), the bulking criteria is different. That is, each request of interest compensation or fee payment (for example, category purpose code is FCOL or INTE or FCIN) is grouped into a separate bulk (that is, one pacs08 per bulk). But, this can still be grouped under one outgoing file (ICF).

[Retrieving Original Credit Transfer](#)

During an incoming return, when a camt.056 or camt.029 message is received, the original credit transfer message is retrieved based on the following conditions:

- Transaction amount
- Settlement date
- Original transaction ID in the R-transaction against transaction ID (original payment)

[Handling PSR (pacs.002s2)](#)

The pacs.002s2 clearing status report for the SCT messages sent to clearing (pacs.008, pacs.004, camt.056, camt.029, camt.027, camt.087 and camt.029) is sent to the originator bank. The payment clearing status report (pacs.002s2) can be classified into three types of acceptance and rejection:

| Level | Description |
| --- | --- |
| File | Can be a complete file acceptance or rejection. |
| Bulk | Denotes the bulk-level acceptance or rejection of the outward credit transfer message sent to the clearing.  - Some bulks are fully accepted or rejected - Some payments within the file are accepted while others are rejected. |
| Transaction | Provides information on the number of transactions accepted and rejected inside the bulk. Payment information details are provided for the rejected transactions. |

The clearing status report received can be a processed STP or Non-STP. It is parked for manual action based on the reason code in the incoming pacs.002s2 (this is done by configuring the *RouteToException* field to Yes). The user can take manual actions, such as resubmit, reject or return the transaction from the Sent Exception page. The user can resubmit or reinitiate the clearing of rejected camt.027, camt.087 or camt.029 message from the enquiry again.

**Receiving Clearing Status Report (pacs.002s2) and Forwarding to Indirect Participant Bank**

When a pacs.002S2 reject message is received for an outgoing pacs.008 , pacs.004, camt.056 (cancellation request) and camt.029 (resolution of investigation) originated from IP (based on the parameterisation in TPH), it moves the rejected transactions to the Sent Exception page for manual intervention. This enables the bank users to perform the following actions:

| Action | Description |
| --- | --- |
| Resubmit | The user performs the following actions:  - Cannot resubmit the   camt.056 or camt.029 message to the clearing, as it displays an error message - Can resubmit the   pacs.008 or pacs.004 message to the clearing |
| Return or Reverse | The Clearing performs the following:  - Rejected pacs.004, camt.056 or camt.029   is forwarded as pacs.002s2 to the IP - Rejected pacs.008 is sent as pacs.004 to the   IP |

[Handling Clearing Cancelled Report (CCF) from STEP2 in pacs.002s2 Format](#)

STEP2 generates Cancelled Credit Files (CCF) for,

- Credit transfers cancelled in the clearing session due to reasons such as lack of funds, suspension of either sender or receiver of CT/RCT transactions, or no clearing processing.
- Reporting any transaction cancelled during the settlement process and automatically resubmitted to the next available settlement cycle for those participant having opted for this configuration.

TPH does not support such Cancelled Credit Files (CCF) generated from the STEP2 service. TPH receives and marks the status of file as ‘NOTPROCESSED’.

[Indirect Participation in SEPA](#)

- TPH as an indirect participant bank can be configured to initiate or receive SEPA payments.
- TPH as a direct participant bank can receive and send SEPA payments from an indirect participant bank or route it to clearing (EBA).

[Enquiries to View the Sent or Received CT File](#)

TPH has the enquiries to view all the Direct Debit (DD) or Credit Transfer (CT) files received from IP or Clearing channel. The user can navigate to the bulk level enquiry from the file level enquiry and further transaction level enquiry.

[Enquiry to View Unmatched R-Messages](#)

- To list the CT return transactions (pacs.004) in repair status (status code - 235) with ‘Original Transaction is Not Found Error’ or ‘Transaction Not in Completed' status, go to **Payment Inquiries**>**Pending Payments**>**Pending Unmatched R-Payments Enquir**y.
- Enter the FT number of original transaction in the *Original Transaction Reference* field, when releasing the payment from general repair queue or new inquiry.

- This field is mapped to *OriginalorReturnId* field in `POR.Supplementary.Info` table.
- TPH validates whether the entered FT number exists in the system and is in ‘Completed’ status.
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
| Submission and Supervisor approval | Performs the following validation:  - On submission of payment, it waits for Supervisor’s approval.  - Once approved, it is moved for further processing. - If rejected, it is modified and resubmitted for approval.  - It is then sent to TPH Engine for further processing. - Payments received in TPH from external banks in STP mode do not wait for Supervisor’s approval. |
| Warehouse | Warehouses payments with future execution date and releases on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement, which is performed in the site. TPH solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (STEP2), which is configured to route to SEPA payment.   Clearing channel determines the message type (pacs.008). |
| Dates calculation | Calculates the payment value and booking dates, which is configured to current date (similar to the execution date) |
| FX calculation | Applies when customer account and payment account currencies are different. If FX shifts are involved, it adjusts value date forward and warehouses the payment.   This feature is supported with Payments Hub (PH) license. |
| Balance reservation | Reserves funds on the debit account. It is done on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. |
| Duplicate check | Performs duplicate check on payments received from ordering or indirect participant bank for a set of payment attributes, such as payment amount, currency and transaction reference.  To know more, refer to Duplicate Check section. |
| Posting | Debits the payment amount and any charges to be borne by the customer to the debtor account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (automatic retry, reject or cancel).  - If Account Management System (AMS) is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward payments are entries made before sending pacs.008 to Clearing.  - Child transaction entries  - Debit debtor account (or ordering bank account) - Credit suspense account  - Settlement transaction entries (bulk)  - Debit suspense account  - Credit EBA clearing Nostro account |
| SEPA channel validations | Ensures the payment meets the compliance requirements of SEPA. |
| Outward payment generation | Generates pacs.008 message. |
| Error queue | If an error occurs while processing SEPA payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

[Inward Processing of SEPA Credit Transfer (pacs.008) Payment Request Received from STEP2 EBA Clearing](#)

This section describes the inward processing of a payment received from clearing in TPH account or another bank (indirect participant).



| Activity | Description |
| --- | --- |
| SCT payment received from clearing network | Receives an inward payment pacs.008 from clearing in TPH. |
| SEPA-specific format validations | Performs SEPA-specific validations on the payment.  If the incoming payment is related to fee payment (for SEPA enquiry), FATF and WTR2 check are relaxed. |
| Account validation | Validates the beneficiary account for the following:  - Number is invalid - Closed - Stopped |
| Dates calculation | Receives SEPA payments with value date configured as current business date. Payment is processed immediately. |
| Filtering | Performs filtering of payments (if configured). This is a bank-specific requirement, which is performed in the site. |
| Fee calculation | Debits charge associated with payment from the customer account. |
| Duplicate check | Performs duplicate check on payments received from SEPA for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | Raises the following accounting entries for an incoming pacs.008:  - Settlement entry (bulk)  - Debit clearing Nostro - Credit suspense account  - Child transaction  - Debit suspense account - Credit customer account |
| Payment archived or redirected to indirect participant | Routes the payment to the IP bank (when the incoming pacs.008 final beneficiary is an IP) or marks it as completed. |
| Error queue | If an errors occurs while processing a SEPA payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

[](#)[STEP2-specific Channel Validations](#)

TPH performs the following channel validations for all customer transfer payments routed to STEP2.

The incoming customer transfer payment could be received from any channel or originated from OE.

- The agents below should not be present in the received payment
  - Reimbursement (Instructing, Instructed, or Third) Agent
  - Previous Instructing Agent
  - Intermediary Agent
- Charge option should not be BEN or OUR
- Debtor and Creditor Agent BIC should always be present in the received payment
- Debtor and Creditor Agent Account details should not be present in the received payment
- If the following information are received in the message, the payment should not be routed to STEP2 as the relevant tag is not present in STEP2 pacs.008 and information could be lost:

- Instruction for Creditor Agent
- Instruction for Next Agent
- Regulatory reporting details
- Related Remittance Information
- Structured Remittance Information.

- Debtor and Creditor account is mandatory and should have IBAN structure
- Transaction Amount should be greater than 0 and less than 1000000000
- Transaction currency should be EUR
- Originating or Beneficiary Bank should be in EU/EEA region

[STEP2-specific Channel Validations for pacs.004](#)

TPH performs the following channel validations for all return transfers routed to STEP2. The return transaction could be received from any channel.

- Returned Instructed amount can be present only if the return reason code is FOCR
- Details of charges should be SHA
- Return reason code should be a valid code acceptable by STEP2
- Additional Information is allowed only for the FOCR return reason code
- Previous Instructing Agents should not be populated in the return transactions for STEP2
- Intermediary Agents should not be populated in the return transactions for STEP2

[Unstructured Address Mapping](#)

The number of unstructured address lines for debtor and creditor in the incoming message formats from various clearings and client channels can be different.

- CBPR+ pain.001 has three lines each of 70 characters
- CBPR+ pacs.008 has three lines each of 35 characters

When sending a pacs.008 message through STEP2, only two lines of 70 characters each is allowed. In order to send as much information as possible in the STEP2 pacs.008 message, TPH merges the available address lines (with space as separator) and maps them as two lines of 70 characters in the outward or redirected pacs.008 file sent to STEP2 clearing.

The following example table shows unstructured address mapping:

| Address Lines Received in CBPR+ pacs.008 | Address Lines Mapped in Outgoing STEP2 pacs.008 |
| --- | --- |
| <AdrLine 1>13/1,HOOGSTRAAT,LEFT PREMIUM TOWER  <AdrLine 2>CROSSCUT STREET,CHITTAGONG PROVINCE  <AdrLine 3>BRUSSELS,1000 | <AdrLine 1> 13/1,HOOGSTRAAT,LEFT PREMIUM TOWER CROSSCUT STREET,CHITTAGONG PROVINCE  <AdrLine 2>BRUSSELS,1000 |

The address mapping logic is also applicable for pacs.004 message.

[Supporting Continuous Gross Settlement Model](#)

Continuous Gross Settlement (CGS) model is a real-time settlement model offered by STEP2 for its participants to settle SEPA CT and DD. CGS is not directly accessible to direct participants, instead an internal interface handles communication between CGS and other STEP2 services.

[Liquidity Management Report](#)

LMR is an optional XML file in the form of camt.053 generated and sent to all the configured CGS Settlement BICs (STEP2 Preferred Agent or Direct Participants). LMR is sent by the STEP2-CGS at the end of each Liquidity Adjustment Checkpoint (LAC) in order to notify about their liquidity position at the beginning and end of the relevant LAC.LMR files also include all the operations that have affected the liquidity position of the CGS Settlement BIC during the LAC.

TPH does not receive and process LMR files.

[Liquidity Notification Report](#)

The CGS module generates LNR (an optional XML file) and sends to all the configured CGS Settlement BICs (STEP2 Preferred Agent Direct Participants) to be notified.STEP2 CGS sends liquidity adjustment notifications if there are funding or defunding actions occurring in the CGS position accounts. CGS sends the notifications called as LNR in the form of camt.054 to the account holding direct participant (as identified through CGS Preferred Agent).

CGS sends LNR when thresholds are exceeded. The Liquidity Notification File also includes a camt.052 bulk to notify the participant that its liquidity position has exceeded the upper or lower thresholds set in the liquidity agenda for the current LAC.

TPH supports only LNR report (camt.054). LNR file, camt.052 are marked with status REJECTED.

[Liquidity Transfer Advice](#)

TPH has the ability to receive LNR from the STEP2 CGS system. TPH considers LNR as LTA, qualifies the LNR as a payment based on business rules, derive accounts for the market accounts within the notification and book them as payment Booking allows the bank to maintain the position of CGS Nostro account in-line with the account within CGS.

LNR may represent a credit advice or a debit advice depending on whether the participant banks account is credited or debited in the CGS Position Account due to liquidity transfer operations between the accounts.

- LNRs that fail processing are moved to the repair queue.
- LQ license is required to receive and process the LTA from STEP2.

[Qualifying the LNR as Payment:](#)

When TPH receives a camt.054, it checks whether the transaction can be determined as payment or not based on the configurable criteria. The user can configure the qualification criteria using the following menu:

**Admin Menu** > **Payments** > **Liquidity Management** > **LTA Qualification**

| Criteria | Description |
| --- | --- |
| Sending Institution Identification | ID of the sending institution. |
| Receiving Institution Identification | ID of the receiving institution (typically a BIC of the bank). |
| Participant Identification | - Identification of the participant whose liquidity position or balance has been adjusted - This is the BIC of the bank (STEP2 preferred agent), in which the receiving bank is a direct participant or liquidity serviced participant. |
| Account Identification | Account of the participant whose liquidity position or balance has been adjusted (bank identifier or an account)  This is the account (held in STEP2-CGS), where receiving banks are a direct participant or liquidity serviced participant |
| Advice Type | Indicates whether the LTA is for a debit operation or credit operation   - Debit Indicator (DBIT) indicates debit on our account (found in the Debtor Account field in LTA) - Credit Indicator (CRDT) indicates credit on our account (found in the Credit Account field) |
| Transfer Type | Type of the underlying transfer, such as Regular Payment, AS transfer, or Liquidity adjustment |
| Local Instrument Proprietary | Identifies the proprietary type of underlying transaction. The values can vary by STEP2. For example, LIIA and LIIE |
| Local Instrument Code | Clearing-specific codes as received. For example, LIQT and LIQE |
| STEP2 Status Code | Status of the adjustments as recorded within the STEP2 system. For example, BOOK |
| Debtor Agent | Identifier of the agent who is getting debited. This can be STEP2 identifier (BIC) or the bank settlement’s BIC with TARGET2 (or the liquidity provider’s settlement BIC) depending on the LTA being debited or credited. |
| Debtor Account | Account identifier of the debtor agent who is getting debited. This can be STEP2 account or the account with STEP2 (or any of the liquidity serviced participant’s account in case the bank provides such service) depending on the LTA being debited or credited. |
| Creditor Agent | Identifier of the agent who is getting credited. This can be STEP2 Identifier (BIC) or the bank settlement BIC with TARGET2 (or the liquidity provider’s settlement BIC depending on the LTA being credited or debited. |
| Creditor Account | Account identifier of the creditor agent who is getting credited. This can be STEP2 account or the account with STEP2 (or any of the liquidity serviced participant’s account in case the bank provide such service) depending on the LTA being credited or debited. |

[Deriving Accounts for LNR:](#)

For the LNR considered as a LTA, if qualified as a payment, the account for which the LNR notification is received is debited or credited in the participant bank that receives during the processing of the LTA payment.

LNR payment comprises a debit account and a credit account that represents accounts where the liquidity adjustments were affected by the Account Holding Institution. Both these accounts are external accounts to the bank, hence TPH resolves these accounts to an in-house Nostro or technical account within the bank to perform necessary bookings. The posting is mainly for liquidity management purposes, such that receiving participant bank’s Nostro balances are up-to-date with the balance or positions in the actual account in STEP2, enabling the receiving participant bank to perform efficient liquidity management functions.

The user can configure the in-house Nostro or technical account in account mapping table from the following menu

**Admin Menu** > **Payments** > **Liquidity Management** > **LTA Account Mapping**

[Handling LNR from Repair Queue](#)

Incoming LNR’s that failed to qualify as a payment or failed while resolving the account or failed duplicate check are moved to a repair queue for repairing by the bank user. Banks can also make the LNR payments as non-STP and can process from the repair queue. The user can view the incoming LNR’s awaiting repair using the dedicated enquiry –LTA Repair in TPH (Read the [Working with](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm) section for more information) .

From the repair screen, the user can either cancel the LNR or modify and submit to continue processing with repaired details.

The following fields can be modified during the repair:

- Value Date
- Debit Account
- Credit Account

Once the user repairs the payment and commits, it is moved to the supervisor’s queue for authorisation (if configured). After authorisation, the repaired payments is processed by the user again starting from the LTA qualification step.

If the user cancels the LNR, the LNR is moved to cancelled (997) status on authorisation. The user must enter the reason for cancelling.

Read the [Liquidity Transfer Advice](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm) guide for more details on configuring, viewing, and repairing LNR.

## Illustrating Model Parameters

To know more on parameter setup for Single Euro Payments Area (SEPA) credit transfer, refer the [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

This module provides the facility to send and receive SEPA credit transfers from STEP2 and RPSSCL clearing.

In this topic

- [Introduction to SEPA Credit Transfer](#IntroductiontoSEPACreditTransfer)

- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm)
- [APIs](../../APIs/Misc/APIs.htm#EP)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:19:35 PM IST