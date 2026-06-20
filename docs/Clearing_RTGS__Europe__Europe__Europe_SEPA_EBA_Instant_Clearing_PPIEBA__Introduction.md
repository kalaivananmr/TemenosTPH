# Introduction to SEPA Instant Clearing - EBA INST

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
    - [Introduction](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
    - [Configuration](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Configuration.htm)
    - [Working with](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Working_with.htm)
    - [Tasks](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Tasks.htm)
    - [Outputs](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Outputs.htm)
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

# Introduction to SEPA Instant Clearing - EBA INST

Updated On 10 July 2025 |
 35 Min(s) read

Feedback
Summarize

The Single Euro Payments Area (SEPA) Instant Credit Transfer (EBA INST) is a payment scheme from the European Payments Council (EPC). It can perform the following:

- Deliver a pan-European instant payment service
- Allow payment service providers (in SEPA) to offer a SEPA-wide Euro instant credit transfer product to its customers

- EBA INSTANT module in Temenos Payments Hub is compliant to ‘EBA RT1 System SCT Inst Service Specifications – 2025’’.
- EBA INST credit transfers have a roundtrip timeframe of 10 seconds within which the instant payment is completed.

## Types of Payment and Messages

TPH supports the following message types used in EBA INST payments flow:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.08 | B2B | Interbank customer credit transfer messages | Inward and outward |
| camt.056.001.08 | B2B | Request for cancellation/ Request for recall by Originator (RFRO) | Inward and outward |
| pacs.004.001.09 | B2B | Return payment | Inward and outward |
| camt.029.001.09 | B2B | Resolution of investigation | Inward and outward |
| camt.029.001.09 | B2B | Response to inquiry messages | Inward and outward |
| pacs.028.001.03 | B2B | Request for status update | Inward and outward |
| pacs.002.001.10 | B2B | Payment status report - Clearing | Inward |
| pacs.002s2 | B2B | Payment status report - PSP | Inward |
| camt.053.001.06 | Statement | Statement of Accounts (SOA) | Inward |
| admi.007.001.01 | Acknowledgement | Receipt of Acknowledgement | Inward |

Following are the customer initiation message (C2B) types:

| Message | Description |
| --- | --- |
| pain.001.001.03, 05 and 09 | Payment initiation from customers, channels or bank upstream systems |
| pain.002.001.03 and pain.002.001.10 | Confirmation messages to customers, channels or bank upstream systems (customer status report) |

Following are the Liquidity Transfer Request (LTR) message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| camt.025.001.05 | Liquidity | LTR response from TIPS | Inward |
| camt.050.001.06 | Liquidity | LTR to TIPS | Outward |
| camt.054.001.06 and camt.054.001.10 | Liquidity | Liquidity transfer advise | Inward |

TPH supports and process the following Clearing files:

| File Name | Description |
| --- | --- |
| Result of Settlement File (RSF) | Optional file that contains payment status bulks corresponding to the original SCT Inst Transactions and R-Messages processed until the end of every LAC |
| Daily Reconciliation Report (DRR) | File sent to EBA INST participants that includes the count and sums of all transactions that a participant sends and receives from the TIPS Clearing |
| Routing Table File (RTF) | File sent at predefined timings by EBA Clearing. It includes the list of all RT1 CS participants, all addressable PSPs, and TIPS reachable entities |

## Architectural Diagram of EBA INST Payments



| Item | Description |
| --- | --- |
| Customer Payment Channels | Source channel of different types of electronic payments (originating from mobile, internet or branch) received from retail and corporate customers. |
| Payment Order Module and Payments Engine | Instant payment processing system in TPH. |
| Temenos Transact or AMS and AML | Bank’s accounting (Temenos Transact or others) and fraud checking systems. |
| EBA INST Clearing System | Instant Payment Clearing Service operated by EBA Clearing in the Euro region. |

## EBA INST Payments Message Flow



The outward message flow in EBA Instant Payments (RT1 Clearing) is as follows:

1. TPH receives a pain.001 from the customer channel to create an instant payment to be sent to the EBA INST channel. Alternatively, an instant payment order is initiated manually from the PAYMENT.ORDER `(PO)` application.
2. If the credit account is in the same bank, TPH creates a book payment and sends the customer status report (pain.002) to the customer channel (after successful processing).
3. To send instant payment to clearing (as an outgoing pacs.008), it performs the following:
   - Validates the debit account
   - Books or reserves the balance based on the configuration
   - Completes timestamping on the payment before sending it to clearing
   - Sends customer status confirmation to the beneficiary customer (if configured)
4. On receiving the confirmation (pacs.002) from clearing, it performs the posting (if not done already) based on the configuration and sends the confirmation to the originating customer.

The inward message flow in EBA Instant Payments (RT1 Clearing) is as follows:

1. TPH receives the instant payment pacs.008 at the beneficiary bank. The system does the time out check based on the configured instant time out setting (around 20 seconds) for EBA clearing.
   - If received within the time out limit, it processes the incoming pacs.008, validates the credit account and sends positive or negative confirmation (pacs.002) to the clearing.
   - If the time out check fails, it rejects the payment with a negative confirmation.
2. If Indirect Participants (IPs) are available, it sends or receives the payment message and confirmations from the Direct Participants (DPs) for further processing.
3. Originating bank sends investigation message (pacs.028) with a positive or negative pacs.002 (clearing status).
4. A recall message (camt.056) is responded as follows:
   - If the beneficiary bank successfully processes the return payment, it sends an honour recall (pacs.004).
   - If the process fails, it sends a dishonour recall (camt.029).

## Types of Participants

The Source, Channel and Clearing settings can be defined separately based on whether TPH is a DP or IP in the EBA INST Clearing scheme (as it supports both). To know more, refer to [Configuration](Configuration.htm) section.

## Time Stamping of Instant Payments

Temenos Payments Hub (TPH) stamps the time of receipt in EBA Instant Payments (RT1) after a successful fund reservation. Time of Receipt (TOR) is the time during which an instruction is received in an application for a payment. TOR is recorded for the following payments as shown below:

- Individual Payments – When an Inst instruction is received by the Originator PSP.
- Bulk Payments – When a bulk transaction is debulked instantaneously.
- Payments with FX – Immediately when the rate is determined. Incase of FX payment, TPH replaces the existing TOR with the time when the rate is determined.
- Manual Payments – When the payment is committed by the user.
- Future Payments – During the configured *Requested Execution Date and Time* corresponding to a future date and time.

- Stamping Time Of Receipt (TOR) is applicable only for clients who have licensed the IPR 2024 (PPEINS) module.
- For non-IPR payments, TPH continues to time stamp instant payments as it is handled currently.
- Read [Instant Payments Regulations - 2024](../EPC004-16_2025_SCT_Instant_Rulebook_v1.0.pdf) for more information on the regulations and enhancements in TPH to comply with the same.

## Dates

TPH does not perform channel cut-off or holiday checks (for example, clearing, currency and country holiday checks) on instant payments, as EBA INST is a 24/7 channel. However, the Debit Value Date (DVD) and Credit Value Date (CVD) can be determined for the instant payment based on the Requested Execution Date from a pain.001 or Requested Credit Value Date (RCVD) from an incoming pacs.008. To know more, refer to [Business Dates](../../Payments_Hub_(PP)/Business_Dates/Introduction.htm#top) section.

## Routing

Transaction amount and payment receipt time influences routing of an instant payment order.

If the transaction amount exceeds the configured product threshold, TPH tries to route the payment via other suitable payment channels (instant or non-instant) in that geography.

An instant payment processed in the Netherlands (NL) can be routed through EBA INST and NL clearing. Hence, the system can route to multiple instant payment channels based on rules.

If transaction amount of an instant payment intended to EBA Instant Clearing exceeds EUR 100.000,00, then TPH tries to route payment via TIPS based on rules.

Some instant payment schemes can have a cut-off time (not 24/7). If the cut-off time is missed, the system routes through another instant/ non-instant payment scheme (as configured) in TPH. To know more, refer to [Routing and Settlement](../../Payments_Hub_(PP)/Routing_and_Settlement/Introduction.htm#top) section.

## Charges

Charge types are mapped to SLEV for instant payments in TPH.

Standard TPH charge calculation logic applies to instant payments.

## Bank Identifier Code (BIC) and IBAN

The preferred party or agent account identifiers in SEPA Instant payments are IBAN and BICs respectively. TPH can derive beneficiary BIC from beneficiary IBAN when a customer payment initiation request (pain.001) is received without beneficiary BIC.

Users can also initiate a SEPA Instant Payment with the debtor and creditor proxy identification in addition to the IBAN. Proxy identification serves as an additional information for the debtor and creditor.

## Clearing Directory and Reachability

EBA provides the Clearing directory file to the RT1 participants at regular intervals and uploads it into the CA.CLEARING.DIRECTORY table in TPH. The system decides on the reachability of the beneficiary BIC based on the following conditions:

- Belongs to the SEPA Instant (EBAINST) scheme.
- Status of the participant as ‘Enabled’.
- Start date indicates the date from which the BIC becomes active and uses the same date in SEPA Instant payments.
- End date indicates the date after which the BIC cannot participate in SEPA Instant payments.

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

The participant bank users can initiate a SEPA payment by providing the structured address details such as *Department*, *Sub-Department*, *Street Name*, *Town Name*, and so on for the debtor and creditor. The participant bank users can also initiate a SEPA payment by providing a hybrid address, that is, structured address details and at least one occurrence of address line.

The user can input either hybrid address or structured address details or unstructured address lines. If structured address details are used, the SEPA payment expects a value for at least *Town Name* and *Country*.



## Investigations

This enables the originator bank to send an inquiry message to clearing, when response is not received from the Instant Payment Clearing after the time out deadline. Clearing can respond to the inquiry or investigation with a positive or negative confirmation (rejection). If the beneficiary bank confirms that funds are available to the Beneficiary and instant payment transactions are successful, then clearing responds with a positive confirmation (which comprises of the following):

- Inquire status of instant payment order
- Originator bank can trigger the investigation message
- Beneficiary can receive investigation from CSM
- Trigger investigation on list of unconfirmed instant payments

## Recalling EBA INST Payment

[Originator PSP](#)

As Originator PSP, EBAINST (RT1) participant can perform the following functions in TPH:

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

The originator bank participant in the Instant Payment Clearing can request recall of a previously settled instant payment transaction within the prescribed number of days following the interbank settlement date. Instant payment clearing forwards the payment cancellation request to the beneficiary bank participant. EBA INST in the beneficiary bank supports the following workflow when the payment cancellation request is received:

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
  - The first occurrence is mandatory and must start with ‘ATR053’ followed by the as per attribute description.
  - When the reject reason code is 'LEGL', the system allows two further occurrences to provide precise reason. The occurrences must start with 'ATR057'.
  - When the reason code is ‘FRAD’ in camt.056, the system allows a maximum of ten further optional occurrences, all starting with ‘FRAD’ followed by the information available to file a legal claim to recover the funds in case of 'Fraudulent originated SCT Inst' reason code.
- If camt.029 used as a ‘Negative Response to the Request for Recall by the Originator’,
  - The first occurrence is mandatory and must start with ‘ATR072’ followed by the information as per attribute description.
  - When the reason code is ‘AC03’ (Wrong IBAN) in camt.056, the system allows a maximum of ten further optional occurrences, all starting with ‘ATR078’ followed by the information as per attribute description.

The user can configure the beneficiary bank to automatically send a negative response (camt.029 with reject code as NOAS) for a recall message received, which has not been responded within the Clearing specified days.

Beneficiary bank can receive a request for status update of an inward cancellation request (originated by both Originator and Customer or by Bank) from the originator bank when the beneficiary bank does not respond to camt.056 within the clearing specified days. If the beneficiary bank receives multiple investigation requests in a file, TPH de-bulks and processes it.

## Liquidity Transfer Advice (camt.054)

EBA RT1 can send Liquidity Transfer Advice (LTA) as camt.054 to the Direct Participants (DP) to notify balance or position update on their RT1 settlement account.

The banks can use RT1-TIPS Instructing Party service to fund its RT1 position in TIPS from the TIPS Dedicated Cash Account (DCA) without connecting to the TIPS clearing. This funding can be directly performed from Temenos Payments Hub or the RT1 application. After the funding is complete, the bank receives the following LTAs:

- A credit notification from RT1
- A debit notification from RT1-TIPS Instructing Party

LTA represents a credit or a debit advice depending upon whether the participant bank’s account is credited or debited in EBA, due to liquidity transfer operations between the accounts.

On receipt of incoming camt.054 from EBA, TPH:

- Stores the LTA
- Qualifies the LTA as a payment
- Resolves the accounts
- Performs posting

LTA payments that fail processing due to format validation or duplicate check failure, or fail to qualify as a LTA, are moved to the repair queue. Refer to the [Qualifying LTA as Payment](Configuration.htm#Qualifyi) and [Deriving Accounts for LTA Payment](Configuration.htm#Deriving) sections in the [Configuring SEPA Instant Clearing - EBA INST](Configuration.htm) topic for more information.

LQ and PPIEBA licenses are required to receive and process LTA from EBA.

[Handling LTA from Repair Queue](#)

Incoming LTA that fail in the following scenarios are moved to the repair queue:

- To qualify as a payment
- While resolving the account
- In duplicate check
- In clearing-specific validations

The user can also change the LTA payments to a non-STP mode and process the payment from the repair queue. The user can view the incoming LTA awaiting repair in the LTA Repair enquiry. Once the user repairs and commits the payment, it is sent for the supervisor’s authorisation (if configured). After authorising the repaired payments, they are processed again starting from the LTA qualification process.

If the user cancels the LTA, it is moved to the cancelled state with 997 status code after authorisation. The user must enter the reason for cancelling. Refer to the [Repairing Failed LTA](Working_with.htm#Repairin) section in the [Working with SEPA Instant Clearing - EBA INST](Working_with.htm) topic for more information.

## Liquidity Transfer Request for TIPS (camt.050)

Participant banks that have subscribed to the Instructing Party service and are direct participants of both, the EBA RT1 as well as TIPS Clearings, can send Liquidity Transfer Request (LTR) messages through the Instructing Party service. The LTR message (camt.050) is a request to move funds from their TIPS Dedicated Cash Account (DCA) to the Ancillary System (AS) Technical Account in TIPS service, thereby increasing the bank’s EBA RT1 position.

The Instructing Party service executes business validations and sends a camt.025 message against the original camt.050 message to indicate whether the LTR is accepted or rejected.

On receipt of a positive camt.025, Temenos Payments Hub updates the audit trail of the original LTR keeping the LTR in the Completed status. If a negative response is received, the system processes the response either in STP mode or manually based on the configuration. If manual processing is configured, the user can view such LTRs from the following enquiry and perform manual action.

**User Menu > Payments > Liquidity Management > Back Office > LTR > Exceptions > LTR Business Exceptions**

PPIEBA and LQ license are required to process and send LTRs to EBA Instant Clearing.

## Capturing LTR

The user can capture LTRs from the LTR page of the `PO` application and OE screen.

To capture LTR using the `PO` application, go to **User Menu > Payments > Liquidity Management > Front Office > LTR Initiation.**

To capture LTR using the OE screen, go to **User Menu > Payments > Liquidity Management > Back Office > LTR Initiation.**

The user can capture the following fields:

| Field | Description |
| --- | --- |
| *Payment Order Product* | Indicates the product relevant to the channel using which the LTR message is delivered  Available only in the LTR page of the PO application. |
| *Debit Account Number* | Indicates the account number (as maintained in the bank’s books) that is debited. If this field is left blank, it is auto-populated when the External Debit Account field is captured based on the internal-external account mapping |
| *Debit Account Currency* | Indicates the currency of the debit account |
| *Debit Account Name* | Indicates the name of the debit account |
| *External Debit Account* | Indicates the account number (as maintained in the account holding institution) that is debited. If this field is left blank, it is auto-populated when the Debit Account Number field is captured based on the internal-external account mapping |
| *Payment Currency* | Indicates the transaction currency  EBA Instant Clearing supports only EUR payments. |
| *Payment Amount* | Indicates the transaction amount |
| *Credit Account Number* | Indicates the account number (as maintained in the bank’s books) that is credited. If this field is left blank, it is auto-populated when the External Credit Account field is captured based on the internal-external account mapping |
| *Credit Account Currency* | Indicates the currency of the credit account |
| *Credit Account Name* | Indicates the name of the credit account |
| *External Credit Account* | Indicates the external account number (as maintained in the account holding institution) that is credited. If this field is left blank, it is auto-populated when the Credit Account Number field is captured based on the internal-external account mapping |
| *Local Instrument Code* | Indicates the clearing-specific Local Instrument Codes |
| *Output Channel* | Indicates the output channel using which the LTR message is delivered  Available only in the LTR page of the OE screen |

## Processing LTR

In addition to normal payment processing, the captured LTRs are subject to liquidity management specific processing, as follows:

| Process | Description |
| --- | --- |
| Account Derivation | External account numbers are maintained with the Account Holding Institution (AHI). Internal account numbers are maintained in the participant bank’s books. These in-house accounts are typically mirror accounts to the external accounts and can either be a Nostro or a suspense account.  During LTR initiation, the user can capture either internal or the external accounts. When the user captures the internal accounts, the external accounts are auto-populated and vice-versa. The user can configure the internal to external account mapping using the A**dmin Menu > Payments > Liquidity Management > LTA Account Mapping** menu. |

Read the [Liquidity Transfer Request](https://docs.temenos.com/docs/Solutions/Payments/Payments/LQ/Payments_Hub_(PP)/Liquidity_Transfer_Request/Introduction.htm) user guide for more information on capturing, processing, and viewing LTRs.

## Outward Processing of EBA INST Payments



| Activity | Description |
| --- | --- |
| Manual capture of EBA INST payment by using `PAYMENT``.``ORDER``(PO)` application | Captures an EBA INST payment from `PO` application page Validates mandatory and non-mandatory fields on submission and displays an error (if any) |
| Payment instructions through customer channels | Customer channels (internet or mobile banking) can send instant payment instructions to TPH bank through `PO` application. The instruction can be in pain.001 format  In the pain.001v09 version, time element is present along with the Requested Execution Date element. The configuration in the `PO` application, allows to warehouse the payment till the Requested Execution Date and Time and then release the payment to TPH for further processing |
| Customer status report | TPH allows user to configure the version of CSR (pain.002) that expected to be generate by the system when specific version of pain.001 (v03 or v05 or v09) is received from the payment channel.  Read [Static Data](../../Payments_Hub_(PP)/Static_Data/Introduction.htm#202212) for more information on configuring Temenos Payments Hub to generate CSR in specific message type. |
| Account validations | Validates the following for ordering account:   - Is a valid Temenos Transact account - Has no posting restrictions - Has sufficient balance to cover the transaction |
| Credit bank BIC validations | Validates the beneficiary bank BIC against EBA INST directory (if configured). If the user has not updated the beneficiary bank BIC, the system derives it based on IBAN (if available) |
| Business validations | Checks whether the instructed amount is empty. If available, the currency needs to be in EUR |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly or indirectly (if configured) |
| Balance reservation | Checks whether the debit account has enough funds to process the payment. If available, it is reserved |
| Submission and Supervisor approval | Performs the following actions:   1. On submission of the payment, it waits for Supervisor approval 2. Once approved, it is moved for further processing 3. The payment is then sent to Temenos Payments Hub Engine for further processing |
| Warehouse | Warehouses the payment with future execution date and releases on the SOD of the execution date  TPH does not support this feature |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site  Temenos Payments Hub solution is pre-integrated with Temenos FCM solution |
| Routing | Routes the payment to a TPH clearing channel (EBA INST) |
| Dates calculation | Calculates the payment value date (if configured) based on RCVD or Requested Execution Date |
| FX calculation | Applies when customer and payment account currencies are different If FX shifts are involved, it adjusts value date forward and warehouses the payment  This feature is supported with Payments Hub (PH) license |
| Balance reservation | Reserves funds on the debit account and is performed on payment amount with charges   - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system |
| Fee calculation | Calculates the applicable charges  Charge mode is set as Shared (SHA) |
| Duplicate check | Performs duplicate check on payments received from an ordering or IP bank for the set of payment attributes, such as payment amount, currency, and transaction reference |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor account. If posting fails due to insufficient funds for an instant payment after account validation and receiving confirmation from clearing, it parks the payment in special queue for manual intervention   - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system   Outward Payments – Entries made before sending pacs.008 to EBA INST   - Debit debtor account - Credit EBA INST clearing suspense account |
| EBA INST channel validations | Timestamps the payment before dispatching to clearing and ensures that it meets the compliance requirements of EBA INST |
| Payment cancellation | Marks the payment as Cancelled, when the instant payment fails in the following:  - Debit account validation - Balance reservation - Filtering - Bank code validation and reachability - Duplication - Routing - Channel validations |

If the originating source of payment from the PO application is Request To Pay (RTP), then it populates the *Purpose* field with RRTP in outgoing SEPA Instant transaction (pacs.008). This links the Request To Pay feature with subsequent SEPA Instant Credit Transfer Payments.

## Inward Processing of EBA Instant Payments



| Activity | Description |
| --- | --- |
| EBA INST payment received from the clearing or from DP | Receives an inward payment pacs.008 |
| EBA INST-specific format validations | Performs the following validations when a payment is received from the clearing house:  - Checks whether AcceptanceDateTimestamp is within the instant payment timeout configuration. - Checks for timestamping only when TPH is a DP, and receives the payment from clearing to either credit a beneficiary in books or forward it to IP. |
| Account validation | Validates the beneficiary account for the following:  - BIC or account number unknown - Closed - Stopped - Not in the currency quoted |
| Credit BIC validation | Validates creditor BIC for an indirect participant. |
| Dates calculation | Calculates the CVD. |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is performed in the site. |
| Fee calculation | Charge bearer is SHA |
| Duplicate check | Performs duplicate check on payments received from EBA INST for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | Debits EBA INST clearing suspense account and posts credit to the beneficiary account or IP Vostro (if TPH is DP). |
| Payment archived or redirected to IP | Redirects the payment to the IP, when TPH is a DP of EBA INST. Payment redirection is a part of agency banking functionality, and is available only with PH license. |
| Payment cancellation | If an error occurs while processing EBA INST payment, it cancels the transaction and sends a negative confirmation to clearing. |

## Reports for EBA INST Payments

[Daily Reconciliation Report (DRR)](#)

This is an optional report with data that allows instant clearing participants to reconcile:

- Transactions sent and received by the SCT instant participant.
- Amounts debited and credited for the relevant processing date.

This report is sent to SCT Instant Participants after midnight of each target day (after 00:00:00 AM).

The DRR also summarises all SCT Instant messages (including R Messages) received by the SCT Instant participant. Payment Hub (PH) accepts the DRR received and provides an interface for the users to view the details of the report.

[Result Settlement File (RSF)](#)

After each Liquidity Adjustment Cycle (LAC) related to real time messages, the IPS creates and sends a RSF (pacs.002IPS) to the originator and beneficiary banks (with the status of transactions related to the instant payments processed). SCT Instant Participant needs to register to avail RSF (optional file). Payment system accepts the RSF received from EBA and offers an interface to view the status of transactions settled in the specific cycle. To know more on reports, refer to [Configuration](Configuration.htm) section.

## Illustrating Model Parameters

To know more on parameter setup for European Banking Authority (EBA) instant transfer, refer the [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

This module provides the facility to send and receive EBA instant transfers from EBA instant clearing.

In this topic

- [Introduction to SEPA Instant Clearing - EBA INST](#IntroductiontoSEPAInstantClearingEBAINST)

- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Architectural Diagram of EBA INST Payments](#ArchitecturalDiagramofEBAINSTPayments)
- [EBA INST Payments Message Flow](#EBAINSTPaymentsMessageFlow)
- [Types of Participants](#TypesofParticipants)
- [Time Stamping of Instant Payments](#TimeStampingofInstantPayments)
- [Dates](#Dates)
- [Routing](#Routing)
- [Charges](#Charges)
- [Bank Identifier Code (BIC) and IBAN](#BankIdentifierCodeBICandIBAN)
- [Clearing Directory and Reachability](#ClearingDirectoryandReachability)
- [Supporting Extended Remittance Information](#SupportingExtendedRemittanceInformation)
- [Payment Order Application (POA)](#PaymentOrderApplicationPOA)
- [Supporting Structured and Hybrid Address](#SupportingStructuredandHybridAddress)
- [Investigations](#Investigations)
- [Recalling EBA INST Payment](#RecallingEBAINSTPayment)
- [Liquidity Transfer Advice (camt.054)](#LiquidityTransferAdvicecamt054)
- [Liquidity Transfer Request for TIPS (camt.050)](#LiquidityTransferRequestforTIPScamt050)
- [Capturing LTR](#CapturingLTR)
- [Processing LTR](#ProcessingLTR)
- [Outward Processing of EBA INST Payments](#OutwardProcessingofEBAINSTPayments)
- [Inward Processing of EBA Instant Payments](#InwardProcessingofEBAInstantPayments)
- [Reports for EBA INST Payments](#ReportsforEBAINSTPayments)
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
Tuesday, April 14, 2026 4:19:30 PM IST