# Introduction to EPC SEPA Credit Transfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/EPC_SEPA_Credit_Transfer/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [EPC SEPA Credit Transfer](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm) > Introduction

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
    - [Introduction](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm)
    - [Configuration](../../Europe/EPC_SEPA_Credit_Transfer/Configuration.htm)
    - [Working with](../../Europe/EPC_SEPA_Credit_Transfer/Working_with.htm)
    - [Tasks](../../Europe/EPC_SEPA_Credit_Transfer/Tasks.htm)
    - [Outputs](../../Europe/EPC_SEPA_Credit_Transfer/Outputs.htm)
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

# Introduction to EPC SEPA Credit Transfer

Updated On 10 July 2025 |
 35 Min(s) read

Feedback
Summarize

EPC Credit Transfer (EPC CT) is a clearing module in Temenos Payments Hub (TPH) that is compliant with EPC guidelines for SEPA Credit Transfers (SCT). This module is offered as an upgrade path for clients who currently use Temenos Funds Transfer (FT) module to connect to local EU clearings to migrate to TPH. Clients can use this module to configure the local clearing in TPH (replacing FT) in a comparatively shorter time frame as the module is already compliant with EPC, the module thereby acting as an accelerator for the upgrade.

- License for the module is PPEPCP.
- The EPC Credit Transfer feature is compliant with ‘SEPA Credit Transfer Inter-PSP Implementation Guidelines 2025 Version 1.0’ specifications.

This feature provides the following functionalities to support banks using European ACH Clearings:

- Default clearing setup under the name EPC.
- Common validations recommended by implementation guideline and rulebook.
- Generating message types as per schema specification.

Additionally, the bank needs to implement the following changes in the system to fully accommodate local clearings:

- Upload clearing directory.
- Configure routing and settlement to route the payments.
- Adjustments to field-level mapping to comply with clearing specifications.
- Additional validations to enforce restrictions on currency, BIC, and IBAN.
- Additional channel-specific validations, if applicable.

[Types of Participants](#)

The participation model offered by SEPA CSMs support direct and indirect participation.

| Participant Type | Description |
| --- | --- |
| Direct Member | A participant bank that exchanges payments directly to the clearing (EBA, Equens, RPSSCL) and holds a settlement account with clearing. |
| Indirect Member | A member bank that exchanges payments with clearing through a SEPA direct member and does not hold a settlement account with SEPA clearing. |

Temenos Payments Hub (TPH) can be configured to act as a SEPA direct participant to directly interact with the SEPA clearing house.

[Types of Payment and Messages](#)

TPH supports the following SCT message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.08 | B2B | Customer credit transfer | Inward and outward |
| pacs.004.001.09 | B2B | Return | Inward and outward |
| camt.056.001.08 | B2B | Payment cancellation request or request for recall | Inward and outward |
| camt.029.001.09 | B2B | Resolution of investigation | Inward and outward |
| pacs.028.001.03 | B2B | Request for status update | Inward and outward |
| pacs.002.001.10 | B2B | Clearing payment status report | Inward |
| pain.001.001.09 | C2PSP | Credit transfer initiation | Inward |
| pain.002.001.10 | PSP2C | Payment status report to customer | Outward |
| camt.087.001.06 | B2B | Request to modify value date | Inward and outward |
| camt.027.001.07 | B2B | Claim non-receipt | Inward and outward |

[Payment Instruments](#)

SEPA payment instrument is SCT.

[Bank Identifier Code (BIC) and IBAN](#)

In SEPA, the preferred methods for identifying banks or branches and beneficiary accounts are IBAN and BIC, respectively. According to SEPA regulations, customers can initiate SCT payments (pain.001) without providing the beneficiary’s BIC. The system derives the beneficiary’s BIC from the beneficiary’s IBAN.

In addition to the IBAN, the user can also initiate a SEPA payment using the debtor and creditor proxy identification, which provides additional information about the debtor and creditor.

[Initiating Customer Credit Transfers](#)

The user can initiate SCT using the following message types:

| Message Type | Description |
| --- | --- |
| pain001 | The system supports both single and bulk pain.001 transactions. These can result in either a book transfer (where the beneficiary is recorded in the processing bank's books) or an outward transfer (where a pacs.008 message is sent to clearing). |
| Payment Order | - The user must enter the ordering and beneficiary customer details, payment amount, payment currency, and either the requested execution date or requested credit value date (calculated based on payment order product configuration). The user then validates and commits the information. - Once the authoriser approves the payment order, the system processes it as either a book transfer or an outward payment, depending on the beneficiary’s location. For outward payments, the system sends a pacs.008 message to clearing. |
| Order Entry (OE) | - The user must enter the ordering and beneficiary customer details, payment amount, payment currency, and debit value date on the OE page. The user then validates and commits the information. - After the authoriser approves the order entry, the system processes it as either a book transfer or an outward payment, depending on the beneficiary’s location. For outward payments, the system sends a pacs.008 SCT reachability message. |

The OE or PO screens are used for customer credit transfers related to fees, charges, or interest payment resulting from enquiries, such as camt.027 or camt.087.

The SEPA clearing house provides the SEPA routing directory file and uploads it to the CA.CLEARING.DIRECTORY table in TPH. The system determines the reachability of the beneficiary BIC based on the following conditions:

- Belongs to the SCT scheme.
- Has a participant status as ‘Enabled’.
- Has a start date that indicates when the BIC becomes active and can be used in SEPA payments.
- Has an end date that indicates when the BIC can no longer participate in SEPA payments..

[SEPA CT Cut-Off Time](#)

The user can send SCT payments to the clearing three days before the requested credit value date. Clearing does not accept any SCT payment received before this period.

[Receiving Incoming Credit Transfer (pacs.008)](#)

You can receive the SCT from clearing, where TPH:

- Receives the pacs.008
- Performs all validations
- Uploads the pacs.008 message to the TPH tables
- Generates accounting entries as shown below.

- Bulk settlement entry

- Debit clearing Nostro
- Credit suspense account

- Child transactions

- Debit suspense account
- Credit customer account

[Returning SCT (pacs.004)](#)

The beneficiary bank can return SCT payments when it is unable to process them. For example, an invalid creditor IBAN, a closed credit account, posting restrictions on the creditor account, and so on. Returns can be processed either automatically or manually, based on the following configuration:

- When a return payment is initiated, TPH reverses the original payment booking and moves it to the ‘Payment Completed with Return (996)’ business state. It then creates and sends a new return payment to clearing, ensuring that the Clearing Nostro is credited.
- When a return payment is received, TPH processes and books it, provided the original payment for the return exists. The initially debited customer is credited, and the original credit transfer is updated to the ‘Payment Completed with Return (996)’ business state.
- When a return payment for the redirected transaction from EPC-based clearing is received, TPH matches it with the original transaction and determines the output channel based on R&S. TPH performs channel validation for the return transaction before sending it out.

[Recalling a Settled Credit Transfer (camt.056)](#)

The originator bank can recall SCT payments sent to clearing by sending a camt.056 (cancellation) recall request message. This request can be initiated by either the originator or the originator bank of the credit transfer. TPH can initiate a cancellation request and specify whether it was initiated by the customer or bank. The system automatically defaults the number of values from the original payment to the cancellation request and the user must update the reason code stating the reason for cancellation. No accounting entries are raised for this message as it is a non-financial message. If TPH, as the beneficiary bank, receives the camt.056 recall request, it can respond with a positive confirmation by sending a pacs.004 return message. The return payment (pacs.004) is initiated by the following:

- Creating a new return transaction
- Debiting a customer account (which was earlier credited by the incoming credit transfer)
- Creating settlement entries to credit the clearing Nostro

The system updates the status of the original credit transfer to ‘Payment Completed with Return (996)’ business state. If the beneficiary bank rejects the recall request from the originator bank, it responds with a negative response by sending a camt.029 Resolution of Investigation (ROI) message. This is a non-financial message that:

- Has no accounting entries raised during the process.
- Is initiated when the reason code for rejection is entered.

The response to an incoming cancellation request can be initiated manually or automatically. After receiving the recall request, the beneficiary bank retrieves the original credit transfer payment associated with the recall.

- If the original transaction is not found, the system rejects the cancellation request automatically based on the configuration.
- If the original credit transfer details are retrieved, the system checks whether the cancellation request can be processed automatically based on the configuration.

[ Example](#)

- If a customer initiates a cancellation request, the system checks whether it falls within the allowed acceptance period. Otherwise, it is rejected by sending a camt.029 message.
- The acceptance period for initiating a cancellation request can be configured separately for customer-initiated and bank-initiated recall requests.

  If the request is within the acceptance period, the system processes the return of the original credit transfer either manually or automatically, depending on the configuration.

TPH allows the user to initiate only one recall for an underlying SEPA Credit Transfer even if the initial recall is unanswered or a negative response received for initial recall.

[Initiating a Bulk Recall Request (camt.056)](#)

TPH can initiate a bulk cancellation request by selecting multiple credit transfers. When the reason code for the cancellation request is provided and bulk cancellation request is authorised, the system generates a camt.056 message.

[Requesting for Status Update (pacs.028)](#)

This non-financial message inquires about the status of the 'Cancellation Request' (camt.056). The originator bank can initiate this status request from the enquiry provided. When the beneficiary bank receives a status update (pacs.028) request, it performs the following:

- If the recall request is already accepted (that is, a return payment is sent to the originator bank), it generates a camt.029 (negative response) with an 'ARDT' status.
- If the recall request is already rejected (that is, a camt.029 is sent to the originator bank), it generates a camt.029 (negative response) with the original reject reason code.

If the bank receives multiple investigation requests in an incoming file, TPH de-bulks and processes it.

The ordering bank sends a status update request (pacs.028) for camt.27 and camt.87, which the beneficiary bank receives and processes. Additionally, the ordering bank can send a request to the beneficiary bank to update the status of an inquiry if they have not received any response.

| Status Update | Description |
| --- | --- |
| Outgoing Request | Allows the user to initiate a status update request (pacs.028) for an outgoing camt.027 or camt.087. |
| Incoming Request | When the system receives an incoming status update request, it checks for a camt.027 or camt.087 request from the originator bank.   - If a matching record is not available, the system updates the status to 'Unmatched'. - If a matching record is found, the system checks whether a camt.029 response is sent for the incoming camt.027 or camt.087 request.   - If a camt.029 response is already sent, the user does not send it again.   - If a camt.029 response is not sent, the user can initiate     the response (manually) from the enquiry. |

[Claiming for Non-Receipt by Originator (camt.027)](#)

The originator or beneficiary of the payment uses the camt.027 message type to send or receive a claim for non-receipt of initial credit transfer. This process occurs when the beneficiary who did not receive the payment contacts the user.

| Message Type | Description |
| --- | --- |
| Outgoing camt.027 | Allows the user to initiate a camt.027 enquiry. This enquiry lists all the outgoing pacs.008 transactions in 'Completed' status, which are sent to clearing.   - When initiating the   camt.027 from the enquiry, the system verifies that the request is initiated within thirteen months of the original credit transfer.   - If the request is initiated outside this time frame, the system displays an error message and does not allow the user to initiate the camt.027 request. |
| Incoming camt.027 | - Processes and uploads the incoming camt.027 message - Allows the user to view the incoming camt.027 message - The system matches the incoming camt.027 with the original pacs.008, which is already processed.   - If the original payment is found and is in a completed state, the system automatically (based on configuration) generates a camt.029 with a status code as ACNR. The system also records the acceptance date of the camt.027 claim and maps the process in the outgoing camt.029.   - If the original payment is found but is in 'Cancelled, Rejected and Returned' status, the system automatically generates (configuration) a camt.029 with a status code as RJNR and reason code as ARDT in the outgoing camt.029.   - If the original payment is not found, the system automatically rejects the camt.029 with reason code as NOOR and status as 'RJNR'.   - If the original payment is not found and the system is configured for manual action, the system parks the camt.027 in the Unmatched queue for manual action.   The user needs to perform the following, when camt.027 is parked for manual action:  - Initiate the Resolution of Investigation - camt.029 message from the enquiry in response to an incoming Non-Receipt claim (camt.027). - Perform an additional   check to verify that the beneficiary bank has responded to the incoming camt.027 within ten days of receiving the message. - Apply claim charges for handling the enquiry. The following values are included in the outgoing cam.029 only when the selected status code is ACNR:   - Charge amount   - Charges BIC   - Charges IBAN - Map and bulk the outgoing camt.029, then generate the file and place it in the output folder. |

[Claiming for Value Date Correction or Requesting to Modify Payment (camt.087)](#)

The originator or beneficiary of the payment uses the camt.087 message type to send or receive a value date confirmation or modification request of initial credit transfer. This process occurs when the beneficiary who claims non-receipt of funds contacts the user on the intended value date. The incoming camt.087 message indicates a modification in the payment due to change in the *Interbank Settlement Date*.

| Message Type | Description |
| --- | --- |
| Outgoing camt.087 | Allows the user to initiate a camt.087 enquiry. The enquiry lists all the outgoing pacs.008 in 'Completed' status, which are sent to clearing.   - When initiating the   camt.087 from the enquiry, the system verifies that the request is initiated   within thirteen months of the original credit transfer.   - If the request is initiated outside this time frame, the system displays an error message and does not allow the user to initiate the camt.087.    The   modified *Interbank Settlement Date* field   is defaulted with original credit value date of the outgoing pacs.008.   - If there is no change in the modified *Interbank     Settlement Date*, then the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields become mandatory.   - If the user updates the modified *Interbank Settlement Date* field to a new date, the *Instruction for Assignee Code* and *Instruction Information for Assignee* fields are no longer mandatory.   Updates the status of camt.087 to 'Claim Sent' status in TPH. |
| Incoming camt.087 | The system performs the following when the beneficiary bank receives a camt.087 message:   - Processes and uploads the incoming camt.087 message. - Allows the user to view the incoming camt.087 message. - Matches the incoming camt.087 with the original pacs.008 that is already processed:   - If the original payment is not found, the system updates the status to 'Unmatched'.   - If the original payment is found, the system checks whether camt.087 is received within the acceptance period.   - If yes, the system proceeds with Straight-Through Processing (STP) of the camt.087 message.   - If not, it parks the incoming camt.087 for manual intervention   - If the original payment is found and is within the acceptance period, the system verifies whether the original payment is in 'Completed' status.   - If yes, it proceeds with STP of the camt.087 message   - If not, it updates the incoming camt.087 status as invalid claim. The system marks the claim as invalid as the original payment is already returned and does not allow modifications to the date in the original payment. Hence, the user cannot perform any manual action as the claim is set as Invalid.   - If the original payment is in 'Completed' status and the *Automated Return Indicator* field is set to Yes, the system checks whether the modified credit value date matches the original credit value date of the pacs.008 transaction.    - If the dates do not match, the system parks the camt.087 request for manual action and updates the status to 'Inwork'.   - If the dates match, the system automatically generates the camt.029 with status as 'RJVA'.   When a camt.087 is parked for manual action, the user selects one of the following responses which determines the camt.029 to be sent:   - Accepted value date adjustment (ACVA) – In this case, the beneficiary bank accepts the new value date because the originator bank sent the original pacs.008 with an incorrect value date. TPH responds with a Resolution of Investigation (camt.029) message using the ACVA status code. After sending the response, the user waits for the payment for interest compensation or charges. Upon receiving the interest payment or charges, reverse the original payment and create a new payment with the new value date as requested by the originator bank. Subsequently, initiate a Resolution of Investigation (camt.029) response with MODI status code. - Modified as per request (MODI) – In this scenario, the beneficiary bank updates the value date based on the request from the originator bank because the delay in the value date is due to the beneficiary bank or Clearing and Settlement Mechanism (CSM). Since the delay is attributable to the beneficiary bank or CSM, compensation is optional. Send the MODI response in camt.029.   Manual Initiation of camt.029 (Accepted ACVA status):   - The user can manually initiate the camt.029 response from the Inward Requests Require Manual Action enquiry. Read the Working with topic for more information. - While processing the camt.029 response, the user can manually enter the compensation and charges amount, if the status is ACVA. Accounting entries are not created for the charges and compensation amounts. This information is mapped to the outgoing camt.029 message. - After sending the ACVA response, the user waits for the payment of interest compensation or charges. - Upon receiving the interest payment or charges, reverse the original payment and create a new payment with the new value date as requested by the originating bank. Then initiate the Resolution of Investigation (camt.029) response with MODI status code.   Manual Initiation of camt.029 (Modified MODI status):   - The user can manually initiate the camt.029 response from the Inward Requests Require Manual Action enquiry. - While processing the camt.029 response, the user can manually enter the compensation and charges amount, if the status is MODI and no earlier response with status ACVA has been provided for the enquiry. - Reverse the original payment and create a new payment with the new value date as requested by the originating bank. Then initiate a camt.029 response with status MODI. |

[Supporting Structured and Hybrid Address](#)

Participant bank users can initiate a SEPA payment by providing detailed structured address information for both the debtor and creditor. This includes fields such as *Department*, *Sub-Department*, *Street Name*, *Town Name*, and so on. The participant bank users can also initiate a SEPA payment by providing hybrid address, that is, structured address details and at least one occurrence of address line.

The user can enter either hybrid address or structured address details or unstructured address lines. If structured address details are used, the SEPA payment requires at least the *Town Name* and *Country* values.

The `PAYMENT.ORDER` application, Order Entry screen, and pain.001 format all support the initiation of SEPA payments using structured address and hybrid address.

The screenshots below display the initiation of SEPA payments in the `PAYMENT.ORDER` application and **Order Entry** screen.





[Supporting Extended Remittance Information](#)

When the system receives a pain.001 file containing both structured and unstructured remittance information, it stores the details in the TPH table. The system retrieves the local instrument code as PERI and checks whether the beneficiary bank's BIC supports the ERI payment option. This determines how structured and unstructured information is mapped in the outgoing pacs.008 message before generating it for clearing.

The TPH system validates and updates the local instrument code PERI from the pain.001 file in the corresponding TPH table. The reachability API checks if the beneficiary bank supports the ERI option based on the local clearing routing table information. During validation, the system ensures that the total character length for structured tags in the ERI payment option does not exceed 280 characters.

- If the incoming pain.001 does not have the local instrument code as PERI, the system updates the TPH table based on the reachability API check.
- If the API returns the value ERI, the system updates the local instrument code as PERI in the TPH table.

| Scenario | Tag |
| --- | --- |
| Outward pacs.008 Mapping | |
| Local Instrument Code is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code is equal to PERI | Maps max 999 occurrences with all structured remittance tags |
| Outward R-messages Mapping (pacs.004, pacs.028, camt.056, camt.029, camt.027, camt.087) | |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:  - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is equal to PERI | Does not map any remittance information |

When initiating and sending outgoing camt.056, pacs.004, camt.029 and pacs.028 messages, the system checks the original payment (pacs.008) for the local instrument code.

- If the local instrument code is PERI, the system does not include structured information in the outgoing camt.056, pacs.004, camt.029, camt.027, camt.087, and pacs.028 messages.

When receiving a pacs.008 message from clearing, the system maps the local instrument code PERI to the respective TPH table and stores the structured remittance information in the remittance information table in TPH.

[PP.ORDER.ENTRY (OE) and PAYMENT.ORDER (PO) Application](#)

Extended Remittance Information (ERI) allows participant bank users to enter up to 999 occurrences of structured remittance information when initiating Credit Transfers (CT) from Payment Initiation (PI) pages. The system splits the information according to the European Payments Council (EPC) guidelines if it exceeds 280 characters (including business and service content). Additional characters are populated in subsequent structured remittance information occurrences when sending an outgoing message to clearing.

The system performs specific validations based on the number of occurrences, before accepting the payments initiated by the user.

[Bulking Criteria](#)

The outgoing file can include multiple transactions of the same message type. The criteria for bulking transactions in the local clearing file are as follows:

- Transaction currency
- Clearing nature code
- Clearing transaction type (CT, RT)
- Credit value date

The bulking logic described above applies to local clearing (currently named EPC). For fee-related payments where the category purpose code is FCOL (Fee Collection), INTE (Interest), or FCIN (Fee Collection and Interest), the bulking criteria differ. Each request for interest compensation or fee payment (such as FCOL, INTE, or FCIN) is grouped into a separate bulk, meaning there is one pacs.008 per bulk.

[Retrieving Original Credit Transfer](#)

During an incoming return, when receiving a camt.056 or camt.029 message, the system retrieves the original credit transfer message based on the following conditions:

- Transaction amount
- Settlement date
- Original transaction ID in the R-transaction against transaction ID (original payment)

[Handling PSR (pacs.002)](#)

The pacs.002 clearing status report for SCT messages sent to clearing (including pacs.008, pacs.004, camt.056, camt.029, camt.027, camt.087 and camt.029) is sent to the originator bank. This payment clearing status report (pacs.002) can be classified into acceptance and rejection:

| Level | Description |
| --- | --- |
| Bulk | Denotes the bulk-level acceptance or rejection of the outward credit transfer message sent to clearing.  - The entire bulk is either fully accepted or fully rejected. - Some payments within the bulk are accepted, while others are rejected. |
| Transaction | Provides information on the number of transactions accepted and rejected inside the bulk. Details of the payment information are provided for the rejected transactions. |

Sending an outward pacs.002 is not supported for credit transfers.

[Enquiries to View Sent or Received CT File](#)

TPH offers enquiries to view all the DD or CT files received from the Clearing channel. The user can navigate from the file level enquiry to the bulk level enquiry and then to the transaction level enquiry.

[Enquiry to View Unmatched R-Messages](#)

To list the CT return transactions (pacs.004) in repair status (status code - 235) with ‘Original Transaction is Not Found Error’ or ‘Transaction Not in Completed' status,

1. Go to **Payment Inquiries**>**Pending Payments**>**Pending Unmatched R-Payments Enquiry**.
2. Enter the FT number of original transaction in the *Original Transaction Reference* field, when releasing the payment from general repair queue or new inquiry.

- The *Original Transaction Reference* field is mapped to the *OriginalorReturnId* field in the `POR.Supplementary.Info` table.
- TPH checks if the entered FT number exists in the system and is in ‘Completed’ status.
- Additionally, TPH allows the release of the transaction from repair without entering the original transaction reference (when the original transaction is not migrated from the legacy system to TPH).

[Outward Processing of SEPA CT (pacs.008) Initiation](#)

This section describes the outward processing of a SEPA SCT payment initiated in a TPH bank, or initiation request received from a customer in the form of pain.001 message.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA credit transfer payment from branch or back office by using PAYMENT.ORDER (`PO`) application or OE page | Captures an SCT payment from the `PO` application or TPH OE page. Validates both mandatory and non-mandatory fields upon submission, and displays any errors if they occur. |
| Payment initiation using pain.001 message | Initiates an SCT by sending a pain.001 message to the ordering bank. |
| Account validations | Validates the following for the ordering account:  - Is a valid Temenos Transact account - Has no posting restrictions - Has sufficient balance to cover the transaction |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly or indirectly (if configured) |
| Balance check (not shown in diagram) | Checks whether the debit account has sufficient funds for the payment to be processed. If funds are available, it reserves the funds required. |
| Submission and Supervisor approval | Performs the following validation:  - Upon payment submission, the system waits for Supervisor approval.   - If the Supervisor approves it, the system moves the payment to further processing.   - If the Supervisor rejects it, the system modifies the payment and resubmits it for approval.  - The system then sends the payment to the TPH Engine for further processing. - Payments received in TPH from external banks in STP mode bypass Supervisor approval and proceed directly to processing. |
| Warehouse | Warehouses payments with a future execution date and releases on the start of day (SOD) of the execution date. |
| Filtering | Filters payments when interfaced with a screening engine, as required by bank-specific needs. This process occurs on-site, and the TPH solution is pre-integrated with the Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (Local Clearing), which is configured to route the SEPA payment.  The clearing channel determines the message type (pacs.008). |
| Dates calculation | Calculates the payment value and booking dates that are configured to the current date (similar to the execution date) |
| FX calculation | Applies when customer account and payment account currencies are different. If FX shifts are involved, the system adjusts the value date forward and warehouses the payment.  This feature is supported with a Payments Hub (PH) license. |
| Balance reservation | Reserves funds on the debit account, including the payment amount and any charges.  - If the Account Management System (AMS) is Temenos Transact, then TPH reserves funds in embedded mode. - If the AMS is external, TPH generates a fund reservation request in standard XML format and processes the response from the external system. |
| Fee calculation | Calculates the applicable charges. |
| Duplicate check | Checks for duplicate payments received from the ordering bank based on a set of payment attributes, including payment amount, currency, and transaction reference.  Read the Duplicate Check section for more information on duplicate checks. |
| Posting | Debits the payment amount and any charges to be borne by the customer to the debtor account. If the posting fails due to insufficient funds, the system parks the payment in the Repair queue for user action, which may include automatic retry, rejection or cancellation).   - If Account Management System (AMS) is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, TPH generates the posting request in native XML format and processes the response from the external system.  Outward payments are entries made before sending pacs.008 to clearing.  - Child transaction entries  - Debit debtor account (or ordering bank account) - Credit suspense account  - Settlement transaction entries (bulk)  - Debit suspense account  - Credit EBA clearing Nostro account |
| EPC common payments validations | Ensures the payment meets the compliance requirements of EPC with a few exceptions.  These exceptions facilitate payments to local clearing systems that use account numbers, sort codes, and non-EUR currencies within the European region. |
| Clearing specific validations | Banks can add additional rules specific to a local clearing system or adhere to the strict rules followed by that local clearing. |
| Outward payment generation | Generates a pacs.008 message. |
| Error queue | If an error occurs while processing a SEPA payment, the system moves the transaction to the Error queue for the user to repair or cancel the payment. |

[Inward Processing of SEPA Credit Transfer (pacs.008) Payment Request Received from Local Clearing](#)

This section describes the inward processing of a payment received from local clearing in a TPH account.



| Activity | Description |
| --- | --- |
| SCT payment received from clearing network | Receives an inward payment pacs.008 from local clearing in TPH. |
| SEPA-specific format validations | Performs EPC-specific validations on the payment.  If the incoming payment is related to fee payments (for SEPA enquiry), the FATF and WTR2 checks are relaxed. |
| Account validation | Validates the beneficiary account for the following:  - Number is invalid - Closed - Stopped |
| Dates calculation | Receives SEPA payments with a value date set to the current business date and processes them immediately. |
| Filtering | Filters payments as configured, based on bank-specific requirements, which are handled on-site. |
| Fee calculation | Debits charge associated with payment from the customer account. |
| Duplicate check | Checks for duplicates in payments received from SEPA based on a configured set of payment attributes, including payment amount, currency, and transaction reference. |
| Credit posting | Generates the following accounting entries for an incoming pacs.008:  - Settlement entry (bulk)  - Debit clearing Nostro - Credit suspense account  - Child transaction  - Debit suspense account - Credit customer account |
| Payment archived | Marks it the payment as completed. |
| Error queue | If an errors occurs while processing a SEPA payment, the system moves the transaction to the Error queue for the user to repair or cancel the payment. |

[EPC Common Payment Validations (pacs.008)](#)

TPH performs the following EPC common payment validations for all customer transfer payments routed to the local clearing system.

The incoming customer transfer payment can be received from any channel or originate from OE.

- The transaction amount must be greater than 0 and less than 1,000,000,000.
- Both debtor and creditor names must be provided.
- If any structured address fields (for debtor and creditor) are filled in, then the town name and country must also be included.
- Structured remittance information is mandatory for fee and compensation payments.

[**Exclusions**](#)

Following are the exclusions in the EPC common payment validations:

- Currency must be EUR.
- Debtor and Creditor IBAN is mandatory.
- Debtor agent and Creditor agent BIC is mandatory.

[Local Clearing Specific Channel Validations](#)

If banks need to perform additional checks based on the local clearing schema or rules, they can incorporate these validations into the Clearing table. These clearing-specific channel validations are applied alongside the standard EPC common payment validations.

[Unstructured Address Mapping](#)

The number of unstructured address lines for debtors and creditors can vary across different incoming message formats from various clearings and client channels.

- CBPR+ pain.001 has three lines each of 70 characters
- CBPR+ pacs.008 has three lines each of 35 characters

When TPH sends a pacs.008 message through local clearing, it allows only two lines of 70 characters each. To include as much information as possible, TPH merges the available address lines (separated by spaces) and maps them into the two lines of 70 characters in the outward or redirected pacs.008 file sent to local clearing.

The following example table shows unstructured address mapping:

| Address Lines Received in CBPR+ pacs.008 | Address Lines Mapped in Outgoing Local Clearing pacs.008 |
| --- | --- |
| <AdrLine 1>13/1,HOOGSTRAAT,LEFT PREMIUM TOWER  <AdrLine 2>CROSSCUT STREET,CHITTAGONG PROVINCE  <AdrLine 3>BRUSSELS,1000 | <AdrLine 1> 13/1,HOOGSTRAAT,LEFT PREMIUM TOWER CROSSCUT STREET,CHITTAGONG PROVINCE  <AdrLine 2>BRUSSELS,1000 |

The address mapping logic also applies to the pacs.004 message.

In this topic

- [Introduction to EPC SEPA Credit Transfer](#IntroductiontoEPCSEPACreditTransfer)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:19:52 PM IST