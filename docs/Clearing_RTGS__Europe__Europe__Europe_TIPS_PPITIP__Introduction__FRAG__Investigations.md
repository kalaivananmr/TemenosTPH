# Introduction to Target Instant Payment Settlement (TIPS) - Investigations

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_TIPS_PPITIP/Introduction.htm#Investigations

---

# Introduction to Target Instant Payment Settlement (TIPS)

Updated On 12 April 2026 |
 29 Min(s) read

Feedback
Summarize

TIPS is a standardised pan-European service with common functionality across different countries and jurisdictions. It can perform the following:

- Setting the payment instantly in central bank money with high capacity and around-the-clock availability.
- Offering instant settlement services in Euro to its participants by extending the services offered by TARGET2 or connecting to any RTGS system.

- TIPS module in Temenos Payments Hub is compliant to TIPS Release R2026.JUN.
- TIPS Payments have a roundtrip timeframe of 10 seconds within which the instant payment is completed.

## Types of Messages

TPH supports the following message types in TIPS payments flow:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.08 | B2B | Interbank customer credit transfer messages | Inward and outward |
| camt.056.001.08 | B2B | Request for cancellation or Request for recall by Originator (RFRO) | Inward and outward |
| pacs.004.001.09 | B2B | Return payment | Inward and outward |
| camt.029.001.09 | B2B | Resolution of investigation | Inward and outward |
| camt.029.001.09 | B2B | Response to inquiry messages | Inward and outward |
| pacs.028.001.03 | B2B | Request for a status update | Inward and outward |
| pacs.002.001.10 | B2B | Payment status report - Clearing | Inward |
| pacs.002s2 | B2B | Payment status report - PSP | Inward |
| camt.053.001.12 | Statement | Statement of Accounts (SOA) | Inward |
| admi.007.001.01 | Acknowledgement | Receipt of Acknowledgement | Inward |

Following are the customer initiation message (C2B) types:

| Message | Description |
| --- | --- |
| pain.001.001.03, 05 and 09 | Payment initiation from customers, channels or bank upstream systems |
| pain.002.001.03 and pain.002.001.10 | Confirmation messages to customers, channels or bank upstream systems (customer status report) |

Following are the Liquidity Transfer Request (LTR) message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| camt.025.001.07 | Liquidity | LTR response from TIPS | Inward |
| camt.050.001.07 | Liquidity | LTR to TIPS | Outward |
| camt.054.001.12 | Liquidity | Liquidity transfer advise | Inward |

## Architectural Diagram of TIPS



| Item | Description |
| --- | --- |
| Customer Payment Channels | Source channel of different types of electronic payments (originating from mobile, internet or branch) received from retail and corporate customers. |
| Payment Order Module and Payments Engine | Instant payment processing system in TPH. |
| Temenos Transact or AMS and AML | Bank’s accounting (Temenos Transact or others) and fraud checking systems. |
| TIPS Clearing System | Instant payment clearing service operated by TIPS clearing. |
| Temenos Payment Solution | Total Temenos solution that has modules, such as PO application and TPH. |

## TIPS Message Flow



The outward message flow in TIPS is as follows:

1. TPH receives a pain.001 from the customer channel to create an instant payment to be sent to the TIPS channel. Alternatively, an instant payment order is initiated manually from the PAYMENT.ORDER (PO) application.
2. If the credit account is in the same bank, TPH creates a book payment and sends the customer status report (pain.002) to the customer channel (after successful processing).
3. To send instant payment to clearing (as an outgoing pacs.008), it performs the following:
   - Validates the debit account
   - Books or reserves the balance based on the configuration
   - Completes time stamping on the payment before sending it to clearing
4. The outgoing message is transported to TIPS through ESMIG (Eurosystem Single Market Infrastructure Gateway) layer. ESMIG layer validates all inbound messages that are meant for routing to TIPS for schema and cross-field validation errors. If any schema error is identified in the message, ESMIG returns an admi.007 message (Receipt of Acknowledgement) as Technical NACK to TPH. On receipt of admi.007, TPH cancels the payment, unwind the reservation and informs the customer.
5. On receiving the confirmation (pacs.002) from beneficiary (for payment transaction within time), TIPS settles the transaction and sends the confirmation of settlement (pacs.002) to the originating customer.

The inward message flow in TIPS is as follows:

1. TPH receives the instant payment pacs.008 at the beneficiary bank. The system does the time out check based on the configured instant time out setting (around 20 seconds) for TIPS clearing.
   - If received within the time out limit, it processes the incoming pacs.008, validates the credit account and sends positive or negative confirmation (pacs.002) to the clearing.
   - If the time out check fails, it rejects the payment with a negative confirmation.
2. If Indirect Participants (IPs) are available, it sends or receives the payment message and confirmations from the Direct Participants (DPs) for further processing.
3. Originating bank sends investigation message (pacs.028) with a positive or negative pacs.002 (clearing status).
4. A recall message (camt.056) is responded as follows:
   - If the beneficiary bank successfully processes the return payment, it sends an honour recall (pacs.004).
   - If the process fails, it sends a dishonour recall (camt.029).

## Types of Participants

The Source, Channel and Clearing settings can be defined separately based on whether TPH is a DP or IP in the TIPS Clearing scheme (as it supports both). To know more, refer to [Configuration](../Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Configuration.htm) section.

## Time Stamping of Instant Payments

Temenos Payments Hub (TPH) stamps the time of receipt in TARGET Instant Payments (TIPS) after a successful fund reservation. Time of Receipt (TOR) is the time during which an instruction is received in an application for a payment. TOR is recorded for the following payments as shown below:

- Individual Payments – When an Inst instruction is received by the Originator PSP.
- Bulk Payments – When a bulk transaction is debulked instantaneously.
- Payments with FX – Immediately when the rate is determined. Incase of FX payment, TPH replaces the existing TOR with the time when the rate is determined.
- Manual Payments – When the payment is committed by the user.
- Future Payments – During the configured *Requested Execution Date and Time* corresponding to a future date and time.

- Stamping Time Of Receipt (TOR) is applicable only for clients who have licensed the IPR 2024 (PPEINS) module.
- For non-IPR payments, TPH continues to time stamp instant payments as it is handled currently.
- Read [Instant Payments Regulations - 2024](../EPC004-16_2025_SCT_Instant_Rulebook_v1.0.pdf) for more information on the regulations and enhancements in TPH to comply with the same.

## Calendar and Holidays

TIPS operates on all days of the week for payments (irrespective of holidays). It is available around the clock, 365 days a year

## Dates

TPH does not perform channel cut-off or holiday checks (for example, clearing, currency and country holiday checks) on instant payments, as TIPS is a 24/7 channel. However, the Debit Value Date (DVD) and Credit Value Date (CVD) can be determined for the instant payment based on the Requested Execution Date from a pain.001 or Requested Credit Value Date (RCVD) from an incoming pacs.008.

## Routing

If the criteria for TIPS payments is not met, TPH routes the payment to other suitable instant payment channels in that geography.

An instant payment processed in the Netherlands (NL) can be routed through TIPS and NL clearing. Hence, the system can route to multiple instant payment channels based on rules.

The maximum amount allowed to be transferred is unlimited, which can be defined for each settlement currency.

In addition, some instant payment schemes can have a cut-off time (not 24/7). If the cut-off time is missed, the system routes through another instant payment scheme (as configured) in TPH. To know more, refer to [Routing and Settlement](../../Payments_Hub_(PP)/Routing_and_Settlement/Introduction.htm#top) section.

## Charges

Charge types are mapped to SLEV for instant payments in TPH.

Standard TPH charge calculation logic applies to instant payments.

## Bank Identifier Code (BIC) and IBAN

The preferred party or agent account identifiers in SEPA Instant payments are IBAN and BICs respectively. TPH can derive beneficiary BIC from beneficiary IBAN when a customer payment initiation request (pain.001) is received without beneficiary BIC.

Users can also initiate a SEPA Instant Payment with the debtor and creditor proxy identification in addition to the IBAN. Proxy identification serves as an additional information for the debtor and creditor.

## Clearing Directory and Reachability

TARGET provides the Clearing directory file to the TIPS participants at regular intervals and uploads it into the CA.CLEARING.DIRECTORY table in TPH. The system decides on the reachability of the beneficiary BIC based on the following conditions:

- Belongs to TIPS.
- Status of the participant as ‘Enabled’.
- Start date indicates the date from which the BIC becomes active and used in TIPS.
- End date indicates the date after which the BIC cannot participate in TIPS.

## Supporting Extended Remittance Information

TPH supports populating extended remittance information details in the outward instant payment when the local instrument code in the payment is PERI and the beneficiary agent supports Extended Remittance Information (ERI) payments (AOS option).

Temenos reachability API returns the local instrument code value as ERI when the beneficiary agent has subscribed for PERI. Based on this response, the local instrument code is updated as PERI in the TPH internal tables.

If the beneficiary agent supports ERI payments, the structured and/or unstructured remittance information is mapped in the outgoing pacs.008 message. The system also validates that the total character length of extended remittance information does not exceed 280 characters.

The table below defines the tags used for the respective scenarios.

| Scenario | Tag |
| --- | --- |
| Outward pacs.008 Mapping | |
| Local Instrument Code is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:   - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code is equal to PERI | Maps max 999 occurrences with all structured remittance tags |
| Outward R-messages Mapping (pacs.004, pacs.028, camt.056, camt.029) | |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is not equal to PERI | Maps the first occurrence of structured remittance for the following tags:   - CreditorReferenceInformationTypeCodeOrProprietaryCode - CreditorReferenceInformationTypeIssuer - CreditorReferenceInformationReference |
| Local Instrument Code in POR.SupplementaryInfo of original transaction is equal to PERI | Does not map any remittance information |

While generating outward camt.056, pacs.004, camt.029, and pacs.028, the system checks the original payment (pacs.008) for the local instrument code. If the local instrument code in the original payment is PERI, then the structured information is not sent in the outgoing camt.056, pacs.004, camt.029 and pacs.028.

## Payment Order Application (POA)

ERI allows participant bank users to enter details (up to 999 occurrences) of structured remittance information when initiating CT from Payment Initiation screens to split the information (based on the European Payments Council (EPC) guideline) when there are more than 280 characters (inclusive of business and service content). This populates the additional characters in subsequent structured remittance information occurrences while sending an outgoing message to Clearing.

The reachability check is not performed when the Domestic Plus version of POA is used for payment initiation.

## Supporting Structured and Hybrid Address

TPH supports the following address formats for the debtor and creditor roles in the SEPA payments (SCT, SDD, and SEPA Instant).

- Unstructured - Address Line 1 and 2 (is supported by schemes until Nov 2026).
- Structured - Address sub-elements (*Town Name* and *Country* being mandatory).
- Hybrid - Structured address (*Town Name* and *Country* are mandatory) and at least one occurrence of address line details.

The participant bank users can initiate a SEPA payment by providing the structured address details such as *Department*, *Sub-Department*, *Street Name*, *Town Name*, and so on for the debtor and creditor. Users (PSPs and PSUs) can also initiate Instant payments by providing a hybrid address, that is, structured address details and at least one occurrence of address line.

The user can input either hybrid or structured address details or unstructured address lines. If sructured address details are used, the SEPA payment expects a value for at least the *Town Name* and *Country*.



## Liquidity Transfer Requests (LTR) for TIPS (camt.050)

Liquidity Transfer Requests can be initiated from the PAYMENT.ORDERapplication GUI by providing *Payment Order Product* as TIPSPAYLTR and *Output Channel* as TIPS. It can also be initiated from the Order Entry application GUI.

TPH supports camt.050 as outgoing LTR initiation message type for TIPS. On receipt of camt.050, TIPS sends a camt.025 to indicate whether the LTR is accepted or rejected. TPH supports processing of camt.025, the inward response message received from TIPS.

Refer [Working With](Working_with.htm#Capturing_TIPS_LTR) section for more information on initiating and authorising LTR for TIPS.

Liquidity Management (LQ) license is required to process and send LTRs to TIPS.

Refer [Liquidity Transfer Request](../../../../Payments/LQ/Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Introduction.htm) user guide for more information on capturing, processing and viewing LTRs.

## Investigations

This enables the originator bank to send an inquiry message to clearing, when response is not received from the Instant Payment Clearing after the time out deadline. Clearing can respond to the inquiry or investigation with a positive or negative confirmation (rejection). If the beneficiary bank confirms that funds are available to the Beneficiary and instant payment transactions are successful, then clearing responds with a positive confirmation (which comprises of the following):

- Inquire status of instant payment order
- Originator bank can trigger the investigation message
- Beneficiary can receive investigation from CSM
- Trigger investigation on list of unconfirmed instant payments

## Recalling a TIPS Payment

[Originator PSP](#)

TIPS participant as Originator PSP can perform the following in TPH:

- Requests to recall a previously settled instant payment transaction within the prescribed deadline that follows the interbank settlement date.
- Sends originator or originator bank user-initiated payment cancellation requests to the Clearing.
- Receives the recall request from an IP (addressable), which it can record and forward to the clearing.
- Initiates cancellation request for one of the following reasons:
  - Request for recall by the Originator (RFRO)
    - Invalid Creditor Account Number
    - Wrong Amount
    - Request By Customer
  - In case of recall
    - Duplicate payment sent
    - Technical problems that result in the erroneous instant payment transaction
    - Fraudulent originated instant payment
  - Allows the user to capture additional information about recall reason in addition to reason code.

Recall needs to be initiated within 10 working days of the original instant payment transaction inter-bank settlement date. If the originator initiates a recall of an instant payment for reasons other than the above, the originator bank:

- Needs to accept the requests within 13 months from the debit date of the original instant transaction.
- Is not obliged to guarantee return of funds and needs to inform the originator.

If the recall is within the prescribed number of days (10 business days for originator bank recall and 13 months for originator) of execution of the initial instant payment transaction, the originator bank participant sends a Payment Cancellation Request (camt.056) message to the beneficiary bank.

The beneficiary bank can do one of the following:

- Accept the payment recall request and return the funds by sending a Payment Return message (pacs.004)
- Refuse the payment recall request and send a Resolution of Investigation (ROI – camt.029 message)

If the beneficiary bank responds within the prescribed period (10 business days following the receipt of the recall message), the originator bank supports the following:

| Responses | Description |
| --- | --- |
| Accepts the cancellation request and sends a payment return | - Processes the incoming return payment (pacs.004) and credits the originator or IP bank account (serviced by the DP) or forwards it to the IP bank (if applicable). - Updates the status of the Payment Cancellation request and records the positive resolution of the cancellation request (that is, updates the details of the payment return message or transaction). - Relays status to the originator according to the agreed terms and forwards the Payment Return message to IP. |
| Sends a negative answer (that is Resolution of Investigation message), as a response to the cancellation request | - Updates the status of the Payment Cancellation request and records the negative resolution of the cancellation request (that is, updates the details of ROI received including the reason for rejection). - Relays status to the originator or IP according to the agreed terms and conditions. |

- TPH allows the user to initiate only one recall or RFRO for an underlying SEPA Instant Credit Transfer even if the initial recall or RFRO is unanswered or a negative response received for initial recall or RFRO.
- The user can initiate a request for status update of an outward cancellation request sent (both originated by Originator/Customer or by Bank), when no response is received from the beneficiary bank within the clearing specified days.

[Beneficiary PSP](#)

The originator bank participant in the Instant Payment Clearing can request recall of a previously settled instant payment transaction within the prescribed number of days following the interbank settlement date. Instant payment clearing forwards the payment cancellation request to the beneficiary bank participant. TIPS in the beneficiary bank supports the following workflow when the payment cancellation request is received:

1. Verify whether the payment cancellation is received within the prescribed time limit.
2. Notify beneficiary of the payment cancellation request and get consent for returning the money.
3. If the recall is against an instant payment of an IP (addressable) serviced by the receiving beneficiary bank, it records the recall and forwards the payment cancellation request to the beneficiary bank.
4. If the beneficiary agrees to return the payment, then perform the following to recall it:
   - Create a new return payment and send to the clearing
   - Update the payment cancellation request as Closed, after updating the return payment details.

   The system supports generation of ISO20022 pacs.004 payment return message.
5. If the beneficiary does not provide consent to return the payment, send a negative answer to the originator bank through clearing.
   - Generate an ROI message (camt.029)
   - Update the payment cancellation request as Closed, after updating the details of the ROI.
6. TPH allows user to populate additional information regarding cancellation reason when sending negative response (camt.029) to a recall request:
   - If cam.029 is used as a ‘Negative response to a Recall’,
     - The first occurrence is mandatory and must start with ‘ATR053’ followed by the information as per attribute description.
     - When the reject reason code is 'LEGL', the system allows two further occurrences to provide precise reason. The occurrences must start with 'ATR057'.
     - When the reason code is ‘FRAD’ in camt.056, the system allows a maximum of ten further optional occurrences, all starting with ‘FRAD’ followed by the information available to file a legal claim to recover the funds in case of 'Fraudulent originated SCT Inst' reason code.
   - If camt.029 used as a ‘Negative Response to the Request for Recall by the Originator’,
     - The first occurrence is mandatory and must start with ‘ATR072’ followed by the information as per attribute description.
     - When the reason code is ‘AC03’ (Wrong IBAN) in camt.056, the system allows a maximum of ten further optional occurrences, all starting with ‘ATR078’ followed by the information as per attribute description.

The user can configure the beneficiary bank to automatically send a negative response (camt.029 with reject code as NOAS) for a recall message received, which has not been responded within the Clearing specified days.

Beneficiary bank can receive a request for status update of an inward cancellation request (originated by both Originator and Customer or by Bank) from the originator bank when the beneficiary bank does not respond to camt.056 within the clearing specified days. If the beneficiary bank receives multiple investigation requests in a file, TPH de-bulks and processes it.

## Processing of Outward TIPS Payments



| Activity | Description |
| --- | --- |
| Manual capture of TIPS payment by using PAYMENT.ORDER (PO) application | Captures an TIPS payment from PO application page. Validates mandatory and non-mandatory fields on submission and displays an error (if any). |
| Payment instructions through customer channels | Customer channels (internet or mobile banking) can send instant payment instructions to TPH bank through PO application. The instruction can be in pain.001 format. |
| Customer status report | TPH allows user to configure the version of CSR (pain.002) that expected to be generate by the system when specific version of pain.001 (v03 or v05 or v09) is received from the payment channel.  Read [Static Data](../../Payments_Hub_(PP)/Static_Data/Introduction.htm#202212) for more information on configuring Temenos Payments Hub to generate CSR in specific message type. |
| Account validations | Validates the following for ordering account:  - Is a valid Temenos Transact account - Has no posting restrictions - Has sufficient balance to cover the transaction |
| Credit bank BIC validations | Validates the beneficiary bank BIC against TIPS directory (if configured). If the user has not updated the beneficiary bank BIC, the system derives it based on IBAN (if available). |
| Business validations | Checks whether the instructed amount is empty. If available, the currency needs to be in EUR. TIPS is designed to be multi-currency and provide settlement in euro and non-euro Central Bank Money when Liquidity Transfer happens to other RTGS systems that are out of scope. |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly or indirectly (if configured) |
| Balance reservation | Checks whether the debit account has enough funds to process the payment. If available, it is reserved. |
| Submission and Supervisor approval | Performs the following actions:  - On submission of the payment, it waits for Supervisor approval. - Once approved, it is moved for further processing. - The payment is then sent to Temenos Payments Hub Engine for further processing. |
| Warehouse | Warehouses the payment with future execution date and releases on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (TIPS). |
| Dates calculation | Calculates the payment value date (if configured) based on RCVD or Requested Execution Date. |
| FX calculation | Applies when customer and payment account currencies are different. If FX shifts are involved, it adjusts value date forward and warehouses the payment. This feature is supported with Payments Hub (PH) license. |
| Balance reservation | Reserves funds on the debit account and is performed on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. Charge mode is set as Shared (SHA). |
| Duplicate check | Performs the check on payments received from ordering or IP bank for the set of payment attributes, such as payment amount, currency, and transaction reference. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor account. If posting fails due to insufficient funds for an instant payment after account validation and receiving confirmation from clearing, it parks the payment in special queue for manual intervention.  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward Payments – Entries made before sending pacs.008 to TIPS  - Debit debtor account - Credit TIPS clearing suspense account |
| TIPS channel validations | Timestamps the payment before dispatching to clearing and ensures that it meets the compliance requirements of TIPS. |
| Payment cancellation | Marks the payment as Cancelled, when the instant payment fails in the following:  - Debit account validation - Balance reservation - Filtering - Bank code validation and reachability - Duplication - Routing - Channel validations |

## Processing of Inward TIPS Payments



| Activity | Description |
| --- | --- |
| TIPS payment received from the clearing or from DP | Receives an inward payment pacs.008 |
| TIPS-specific format validations | Performs the following validations when a payment is received from the clearing house:  - Checks whether AcceptanceDateTimestamp is within the instant payment timeout configuration. - Checks for timestamping only when TPH is a DP, and receives the payment from clearing to either credit a beneficiary in books or forward it to IP. |
| Account validation | Validates the beneficiary account for the following:  - BIC or account number unknown - Closed - Stopped - Not in the currency quoted |
| Credit BIC validation | Validates creditor BIC for an indirect participant. |
| Dates calculation | Calculates the CVD. |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is performed in the site. |
| Fee calculation | Charge bearer is SHA |
| Duplicate check | Performs duplicate check on payments received from TIPS for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | Debits TIPS clearing suspense account and posts credit to the beneficiary account or IP Vostro (if TPH is DP). |
| Payment archived or redirected to IP | Redirects the payment to the IP, when TPH is a DP of TIPS. Payment redirection is a part of agency banking functionality, and is available only with PH license. |
| Payment cancellation | If an error occurs while processing TIPS payment, it cancels the transaction and sends a negative confirmation to clearing. |

[](#)[Clearing Reports](#)

TIPS provides the following types of reports for applicable actors based on subscription:

- Statement of Account (SOA)
- Statement of Account Turnover (SOAT)

The following applicable actors are eligible to receive these statements:

- Participant
- Instructing party on behalf of participant

SOA report provides information on the activities recorded for all TIPS accounts of the recipient actor. TIPS provides the SOA in the following modes based on subscription:

- Full – Time between the start and end of RTGS business day.

TPH supports only Full mode of SOA.

## Inclusion of Distinguished Name

Distinguished Name (DN) is a unique identifier provided by SWIFT to its participants in addition to the SWIFT Bank Identification Code (BIC). The parties involved in the payment have a unique DN and it is authorised by the participant to send and/or receive payments.

The configuration for DN in payment is held in Banking Framework (BFW) layer. When a message is sent out using the Delivery Framework (DE) layer, the system searches the DE.CARRIER table for retrieving DNs of both instructing and instructed party. Temenos Payments Hub calls the DE.GET.DISTINGUISH.NAME API exposed by BFW to retrieve DN of sender's and receiver's instructing parties and include it in the Interaction Framework (IF) event for the network to append the DN in the header of the outgoing messages sent.

Handling DN in inbound payments from Target Instant Payment Settlement (TIPS) clearing is not applicable. SIA network removes the header and forwards only the payload to Temenos Payments Hub.

## Liquidity Transfer Advice (camt.054)

TIPS clearing can send Liquidity Transfer Advices (LTA) to its direct participants to notify balance or position update on their TIPS cash account. The camt.054 message is used as the LTA by TIPS.

An LTA could be a debit or a credit advice depending on whether the bank’s cash account is debited or credited in TIPS because of liquidity transfer operation.

TPH executes the following operations on receipt of an incoming camt.054 from TIPS:

- Stores the LTA.
- Qualifies the LTA as a payment based on configuration.
- Resolves the account in the LTA to a corresponding internal or mirror account in TPH.
- Performs posting.

LTA payments that fail processing (for example, format validation, duplicate check or failed to qualify as LTA) moves to the LTA repair queue. Manual actions can be taken by the user on these payments.

Read the Liquidity Transfer Advice [Configuration](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Configuration.htm) and [Working with](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm) topics for more information.