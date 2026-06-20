# Introduction to Euro Swiss Interbank Clearing (EUROSIC)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_euroSIC_PPESIC/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm) > Introduction

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
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
    - [Introduction](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
    - [Configuration](../../Europe/Europe_euroSIC_PPESIC/Configuration.htm)
    - [Working with](../../Europe/Europe_euroSIC_PPESIC/Working_with.htm)
    - [Tasks](../../Europe/Europe_euroSIC_PPESIC/Tasks.htm)
    - [Outputs](../../Europe/Europe_euroSIC_PPESIC/Outputs.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to Euro Swiss Interbank Clearing (EUROSIC)

Updated On 22 March 2025 |
 40 Min(s) read

Feedback
Summarize

Euro Swiss Interbank Clearing (EUROSIC) is a Real-time Gross Settlement (RTGS) payment system, where each payment is settled individually, irrevocably, and with finality. EUROSIC is a copy of the Swiss franc SIC system that settles euro payments through the accounts of Swiss Euro Clearing Bank (SECB) between participants.

EUROSIC also supports cross border payments in euro currency from anywhere in the Eurozone (through TARGET2 or STEP2) to anywhere in Switzerland and Liechtenstein and vice versa.

The following chart illustrates the process flow of the EUROSIC credit transfer message:



EUROSIC supports the following message types:

| Message Type | Description |
| --- | --- |
| pacs.008.001.02 | Credit Transfer (CT) payments sent out by the originating participant bank to the EUROSIC RTGS system, CT payments received by the beneficiary bank from the EUROSIC RTGS system when forwarded after settlement |
| pacs.009.001.02 | Bank transfer sent from an instructing participant (financial institution) to the EUROSIC clearing system and from the EUROSIC clearing system to an instructed participant (financial institution) |
| pacs.002.001.03 | Process the validation payment status report sent by the EUROSIC RTGS system as a response to outward customer credit transfer request (pacs.008), bank credit transfer (pacs.009) and payment return (pacs.004), outward inquiry request (pacs.028) |
| pacs.004.001.02 | Payment returned by the beneficiary bank in the event of an issue with the credit account or as a positive answer to a recall request |
| camt.056.001.01 | Cancellation request initiated by the originating bank to cancel an outward credit transfer |
| camt.029.001.03 | Generate negative answer to an inward cancellation request or receive negative answer to an outgoing cancellation request |
| camt.027.001.06 | Claim for non-receipt inquiry request initiated by the originating bank to inquire whether an outward credit transfer is executed or not |
| camt.087.001.05 | Request to modify the payment initiated by the originating bank to modify the date value of an outward credit transfer |
| camt.029.001.08 | Generate answer (positive or negative) to an inward inquiry request or receive answer (positive or negative) to an outgoing inquiry request |
| camt.025.001.03 | Generate the cash management receipt (accept or reject) as a response to camt messages, such as camt.056, camt.029, camt.027, and camt.087 |
| pacs.028.001.01 | Request for a status update initiated by the originating bank for a previously sent recall request or inquiry message |

## Type of Participant

A Direct Member is a participant bank that exchanges payments directly to the clearing (EUROSIC), and holds a settlement account (SECB) with clearing.

## Type of Payment and Message

The following table shows the EUROSIC SCT message types supported by TPH:

| Message | Description | TPH Support |
| --- | --- | --- |
| pacs.008.001.02 | Customer credit transfer | Inward and outward |
| pacs.009.001.02 | Financial institution credit transfer | Inward and outward |
| pacs.004.001.02 | Return of credit transfer | Inward and outward |
| camt.056.001.01 | Payment cancellation request or request for recall | Inward and outward |
| camt.029.001.03 | Resolution of investigation | Inward and outward |
| camt.029.001.08 | Response to inquiry messages | Inward and outward |
| camt.025.001.03 | Cash management receipts | Inward |
| pacs.028.001.01 | Payment status request | Inward and outward |
| pacs.002.001.03 | Clearing payment status report | Inward and outward |
| camt.087.001.05 | Request to modify ayment | Inward and outward |
| camt.027.001.06 | Claim non-receipt | Inward and outward |

## Payment Instruments

EUROSIC credit transfer is the EUROSIC payment instrument.

## Identifiers

This section describes the bank and account identifiers used in EUROSIC.

[Bank Identifier](#)

The participants (bank/branch) can either be identified by SIC IID (Institution Identification that is, six digit code; for example, 092052) or Bank Identifier Code (BIC). In case of cross system payments, EUROSIC clearing derives BIC from the given SIC IID (SIC number).

[Account Identifier](#)

The account number or IBAN (International Bank Account Number) serves as a unique identifier for the bank account in EUROSIC payments.

## Initiating Customer Credit Transfers

EUROSIC Credit Transfer can be initiated through the following ways:

[Payment Order](#)

EUROSIC credit transfer can be initiated from the `Payment Order` (PO) application. The user needs to input the ordering customer details, beneficiary customer details, payment amount, payment currency, requested execution date. The requested credit value date is calculated based on the `PO` product configuration. The payment order is validated and the record is committed.

The `PO` application version includes the Cross Border Payment Reporting plus (CBPR+) fields, which is also a part of EUROSIC clearing fields (such as, *Street name*, *Building number*, *Post code* and so on).

The authoriser authorises the payment order and the system processes an outward payment. The pacs.008 message is generated to be sent to clearing.

[Order Entry](#)

EUROSIC credit transfer can be initiated from the Order Entry (OE) screen as well. The user needs to input the ordering customer details, beneficiary customer details, payment amount, payment currency, and debit value date in OE. The OE record is validated and the record is committed. The authoriser authorises the payment order and the system processes the payment. For outward payments, pacs.008 EUROSIC CT Reachability EUROSIC routing directory file is provided by the SWISS Euro Clearing house and the same is uploaded to the `CA.CLEARING.DIRECTORY` table in Temenos Payments Hub and checks for beneficiary bank reachability based on the Scheme, BIC/NCC, and Payment Channel parameters.

## Receiving Incoming Credit Transfer (pacs.008.001.002 or pacs.009.001.02)

The beneficiary bank receives the Credit Transfer (CT) payments from EUROSIC RTGS system. Temenos Payments Hub perform clearing-specific validations and upload the pacs.008 or pacs.009 message to `Payment Order (POR)` tables.

EUROSIC clearing performs the following validations:

- Below are some of the payment types allowed for EUROSIC clearing:

  | For EUROSIC customer credit transfer pacs.008 | For EUROSIC bank transfer pacs.009 |
  | --- | --- |
  | ESRDEB = ISR payment resulting from a direct debit  IPIDEB = IPI payment resulting from a direct debit  SEPPMT = EUROSIC payment (EUR only)  CSTPMT = Generic customer payment  SEPFCP = SEPA fee and/or compensation payment (in EUR only) | F2FPMT = FI to FI Payment  COVPMT = Cover Payment |

- For the SEPPTM payment type, the total settlement amount must not exceed EUR 999,999,999.99.
- For the CSTPMT payment type, the instruction identification must contain Unique End-to-End Transaction Reference (UETR) or Global Payments Innovation (GPI) reference.
- Either account number or IBAN must be present for the creditor and debtor parties to process the payment.
- Structured postal address fields such as, <StrtNm>, <BldgNm>, <PstCd>, and <TwnNm> are not permitted along with the <AdrLine> tag.

A new payment type SEPFCP has been added for pacs.008 which is for SEPA fee and/or compensation payment (in EUR only). As part of that, the payment type SEPFCP has been added in the PO and OA versions. Participant banks can now initiate a customer credit transfer payment (pacs.008) for the SEPFCP type. Since SEPFCP” is a new payment type supported by euroSIC clearing, validation have been added as part of the channel validation. The category purpose code for SEPFCP should have any of the following values: FCIN, FCOL, INTE.

The euroSIC Payment Order Application (POA) has been enhanced with an optional tag settlement time and it is generated as part of pacs.008. The `PAYMENT.ORDER,EUROSIC.CTR.NEW.INPUT` euroSIC POA version screen has been enhanced with the *Time Indication Code Type* field. The user can capture time indication codes specific to euroSIC clearing and an associated multi-value field is used to capture corresponding time value during payment initiation. This field has the following drop down values:

- FromTime: The time from which the settlement happens in clearing.
- TillTime; The time until which the payment can be settled in clearing.
- RejectTime: If the payment is not settled within this time, clearing should reject the payment.
- CLSTime: This is the clearing and settlement time.

When the code word /FROTIME/ is used in a euroSIC order and combined with either one of the code words /TILTIME/ and/or /REJTIME/, Temenos Payments Hub will validate that the indicated /FROTIME/ is less than the /TILTME/ and/or /REJTIME/.

New sub elements have been added for a structured address. Also, new sub elements are added under regulatory reporting as part of the euroSIC 2022 rulebook. The extended address fields are *Department, Sub Department, Street Name, Building Name, Building Number, Floor, Post Box, Room Number, Postal code, Town Name, Town Location Name, District name, Country Sub Division, Country*.

Temenos Payments Hub processes the payment and performs the necessary validation checks (account validation, reservation booking, reachability check and AML check, channel validation and POA validations). On the successful validation, Temenos Payments Hub raises the posting request and also generates a pacs.008 with all address tags and sends the message to the euroSIC system.

Temenos Payments Hub receives and maps the incoming pacs.008. (SWIFT/Eurosic) Temenos Payments Hub process the payment and performs the necessary validations. Temenos Payments Hub determines that the payment will be redirected via SWIFT (LORO/NOSTRO) or SIC. The outgoing message pacs.008 is generated based on the provided mapping containing the roles.

The euroSIC POA has been enhanced with the settlement time request and category purpose code, prop optional tags. These tags will be generated as part of the pacs.009 message.

The settlement time request is allowed for the F2FPMT and COVPMT payment types and the category purpose-code, proprietary are allowed for CMPPMT.

The PmtId/UETR and GPI information new mandatory element has been added in SvcLvl/Cd instead of PmtId/InstrId. The Previous Instructing Agent 2 and Previous Instructing Agent 3 have been added as new elements for pacs.009 and underlying pacs.009cov. The Intermediary Agent1 tag has been extended with 2 and 3 for pacs.009 and underlying pacs.009cov. These are optional tags.

New sub elements have been added for a structured address of all parties’ roles for pacs.009 and underlying pacs.009cov.

New functionality and mapping level changes have been added as part of the euroSIC 2021 and 2022 rulebook changes for the camt.056 and camt.029 messages to adapt CBPR+ usage. Temenos Payments Hub creates an EBQA record for the received camt.056 message and updates the status as Inwork for the EBQA record. The system identifies the pacs.008 transaction as completed. Also, Temenos Payments Hub identifies that the cancellation request is received and verifies the received camt.056 message having all tags as per the mapping.

When the user initiates a return request for a previously sent euroSIC payment which is in completed status (999) using the Customer Initiated/Bank Initiated Cancellation Request enquiry, Temenos Payments Hub will create an EBQA record for the same and will generate an outward camt.056 message to euroSIC clearing as per the camt.056.001.08.ch.02 XSD and with the RB 2022 changes below:

- The Control Data sub-element has been removed.
- The AC03, AGNT, AM09, BE16, COVR, CURR, CUST, CUTA, DT01, DUPL, FRAD, FRNA, INDM, TECH, UPAY, NARR, AC02 new reason codes codes have been added for the return request.
- New elements have been added.
- The Original Message Name Identification tag has been changed.
- The Assignee > Agent > Clearing system identification cardinality has been changed.

When Temenos Payments Hub receives an incoming camt.029 for an already sent camt.05 message, the system will identify the original EBQA record and will validate if the received camt.029 message is as per the updated mapping sheet with the RB 2022 changes below:

- New elements have been added.
- The Original Message Name Identification tag has been changed.
- Additional Information tag changes have been done in the recall response.

The recall camt.056 message (originator bank or customer) will be received with the reason code for the incoming pacs.008 message. The user will need to go to the Inward Cancellation Req-Require Manual Action, select the inward camt.056 message and click on the **Reject** option with the reason code to initiate the negative recall response camt.029 message.

Temenos Payments Hub receives an incoming pacs.002 message with the error code 118 from the EuroSIC clearing for an outgoing pacs.008, pacs.009 or pacs.009cov message. Temenos Payments Hub accepts the message and populates the error code in the *ClearingReasonCode* field of the `PSM.BLOB` application.

Temenos Payments Hub receives and validates the incoming pacs.008, pacs.009 or pacs.009cov file from the EuroSIC clearing.

Temenos Payments Hub sends the outward pacs.002 message with the status as RJCT and reason as 134 or with the status as ACCP to the EuroSIC clearing with the orgnUETR tag the same as the UETR tag in the pacs.008, pacs.009 or pacs.009cov message.

The following elements have been released as part of EuroSIC RB2022:

- Original Creation Date Time.
- Original UETR.
- Original Interbank Settlement Date.

The Return Chain Mandatory element has been released to capture all the parties involved in the return transaction.

The OrgnlUETR separate element will be generated in the pacs.002 outgoing message and, optionally, can be also in the incoming pacs.002 message.

For the following fields, the Unknown value will be displayed in the incoming pacs.002 message if the <TxSts> tag is RJCT and the original transaction is not identified:

- OrgnlMsgId.
- OrgnlMsgNmId.
- OrgnlTxId.
- Instructing Agent> MmbId.
- Instructed Agent> MmbId.

New changes have been released for the camt.029v8 message, in the positive response (PRC087) and confirmed positive response (CPRC087) for the value date correction.

The camt.029.V8 message will be generated. The ACVA code will be available in the Sts+Conf tag for the positive response (PRC087) and the MODI code will be available in the Sts+Conf tag for the confirmed positive response (CPRC087). If the ACVA and MODI codes are available in the Sts+Conf tag, then the RsltnRltdInf or IntrBkSttlmDt tag will be captured. The BH and TE support has been provided for the camt.027, camt.087, camt.029v8 and pacs.028 messages.

The following accounting entries are raised for an inward pacs.008 message.

| Settlement Accounting Entries | Customer Accounting Entries |
| --- | --- |
| Debit EUROSIC clearing nostro account  Credit Internal suspense account | Debit Internal suspense account  Credit Creditor account |

The following accounting entries are raised for an inward pacs.009 message.

| Settlement Accounting Entries | Customer Accounting Entries |
| --- | --- |
| Debit EUROSIC clearing nostro account  Credit Internal suspense account | Debit Internal suspense account  Credit Bank Nostro account |

## Returning EUROSIC Credit Transfers (pacs.004.001.002)

If the beneficiary bank cannot process the EUROSIC credit transfer, it can be returned. Some common reasons include invalid creditor IBAN, credit account is closed, posting restrictions on the creditor account and so on. The beneficiary bank can return the credit transfer automatically or manually based on the configuration.

When the return payment is initiated, original payment’s bookings are reversed and payment is moved to the Payment completed with return (996) business state. A new return payment is created and sent to clearing. This ensures that the clearing nostro is credited.

When a return payment is received, and if the original payment for the return has been received exists, then the received return payment is processed and booked. In this case, the customer who was initially debited, would get credited. The original credit transfer is updated to the Payment completed with return (996) business state.

## Recalling Settled Credit Transfer (camt.056.001.01)

EUROSIC credit transfer sent out to the clearing by the originator bank can be recalled by sending a camt.056 (cancellation) recall request message. The cancellation request can be initiated by the originator of the credit transfer or the originator bank of the credit transfer.

Temenos Payments Hub provides an option to initiate a cancellation request and specify whether it is initiated by the customer or the bank. The system automatically defaults the number of values from the original payment into the cancellation request and expects to provide a reason code. This reason code states the reason why the cancellation is being requested.

No accounting entries are raised for this message as it is a non-financial message.

In case Temenos Payments Hub is the beneficiary bank receiving a camt.056 recall request, it can respond with a positive answer by sending a pacs.004 return message. Return payment (pacs.004) is initiated by creating new return transaction and the customer account is debited, which was earlier credited by the incoming credit transfer. The settlement entries are created to credit the clearing Nostro. The status of the original credit transfer is updated with Payment completed with return (996) business state.

The beneficiary bank can respond with a negative response by sending a camt.029.001.03 resolution of investigation (ROI) message indicating that it is rejecting the recall request received from the originator bank. The camt.029.001.03 message is also a non-financial message and no accounting entries are raised during this process. The camt.029.001.03 message is initiated, where the reason code for rejection is entered.

The response to an incoming cancellation request can be initiated either manually or automatically. When the beneficiary bank receives the recall request, it retrieves the original credit transfer payment for which the recall has been received.

- If the original transaction is not found the cancellation request is rejected automatically based on the configuration.
- If the original credit transfer details are retrieved, the system checks if the cancellation request can be processed automatically based on the configuration. (If the *AutoReturnIndicator* flag is set to N, then the cancellation request is parked for manual action else cancellation request is processed automatically to return the original credit transfer using pacs.004).
- If the cancellation request was initiated by the customer, the system checks if the cancellation request is within the acceptance days else the cancellation request is rejected by sending a camt.029 message. If it is within the acceptance days, then the system performs the return processing of the original credit transfer either manually or automatically as explained above.
- The acceptance day’s check to initiate a cancellation request can be configured for both customer initiated recall request and bank initiated recall request.

## Request Status Update (pacs.028.001.01)

Request for status updated (pacs.028) message can be sent to enquire the status of the cancellation request (camt.056). The originator bank can initiate a status update request from the provided enquiry. This is a non-financial message.

When the beneficiary bank receives a request for status update (pacs.028), following is performed:

- If the recall request was already accepted (that is, a return payment was sent to the originator bank), then a camt.029.001.03 (negative response) with ADRT status must be generated as a response to the request for status update.
- If the recall request was already rejected (that is, a camt.029 was sent to the originator bank) then a camt.029.001.03 (negative response) with the original reject reason code must be generated again as a response to the request for status update.

Request for Status Update (pacs.028) for camt.27 and camt.87 can be sent by ordering bank, received and processed by the beneficiary bank. The originator  bank  can  send  a  request  for  status  update  to  the beneficiary bank for an inquiry sent earlier which the beneficiary bank has  not yet replied.

[Outgoing Request for Status Update](#)

To initiate a status update request (pacs.028) for an outgoing camt.027 or camt.087 message, go to **User Menu**>**Payments**>**Payments Hub**>**Investigations & Cancellations**>**Cancellations**>**RTGS Cancellation**>**Outward Cancellation Request Update.**

[Incoming Request for Status Update](#)

When an incoming request for status update is received, the system checks whether a camt.027 or camt.087 request was received already from the originator bank and performs the following steps:

1. If a matching camt.027 or camt.087 record is not available, the system updates the status to UNMATCHED.
2. If a matching camt.027 or camt.087 record is found, the system checks whether a camt.029.001.008 response has been sent already as a response for the incoming camt.027 or camt.087.
   1. If the camt.029.001.008 response was sent already, the same camt.029.001.008 message is sent again automatically with a new case ID to avoid duplicate check.
   2. If camt.029.001.008 response was not sent, the user can initiate the camt.029.001.008 response manually from the enquiry.

## Claim of Non-receipt by Originator (camt.027.001.06)

Claim of Non-Receipt (camt.027.001.06) is for the originator or beneficiary of the payment to send or receive a claim of non-receipt of initial credit transfer, as the originator or beneficiary was contacted by the beneficiary claiming non receipt.

[Outgoing camt.027 Message](#)

The user can initiate a camt.027 message from the provided enquiry. The enquiry lists all the outgoing pacs.008 which are in completed status and sent to clearing.

While initiating the camt.027 from the enquiry, the system checks whether the camt.027 request is initiated within 13 months of the original credit transfer. If the camt.027 is initiated outside the parameterised time frame, an error message is displayed and user cannot initiate the camt.027 message.

[Incoming camt.027 Message](#)

The following are performed on an incoming camt.027 message:

- The incoming camt.027 message is processed and uploaded.
- Enquiry is provided to the user to view the incoming camt.027 message.
- The system matches the incoming camt.027 with the original pacs.008, which was already processed.
- If the original payment is found and is in a completed state, the system automatically generates the camt.029 message with ACNR status code and the acceptance date on which the camt.027 claim was accepted and processed is mapped in the outgoing camt.029 (v8.0) message.
- If the original payment is found and is in cancelled, rejected, and returned status, the system automatically generates (configuration) the camt.029 message with RJNR status code and ARDT reason code in the outgoing camt.029 message.
- If the original payment is not found, it can be rejected automatically by sending a camt.029 (v8.0) message with reason code as NOOR and status as RJNR.
- If the original payment is not found and the system is configured for manual action, the camt.027 message is parked to the UNMATCHED queue for manual action.

If the camt.027 message is parked for manual action, the following can be performed:

- From the enquiry, the user can initiate the camt.029 (v.8) message in response to an incoming camt.027 message.
- Additional check is performed to check if the incoming camt.027 message is responded by the beneficiary bank within 10 days of the receipt of the camt.027 message.
- Outgoing camt.029 (v8.0) message is mapped and the file is generated in the output folder.

## Claim Value Date Correction or Request to Modify Payment (camt.087.001.05)

Claim of value date correction or request to modify payment (camt.087.001.05) is for the originator or beneficiary of the payment, to send or receive a value date confirmation or modification request of initial CT. This is performed when the originator or beneficiary is contacted by the beneficiary claiming non-receipt of funds on the intended value date.

The incoming camt.087 message is to indicate a modification in the payment with respect to change in the interbank settlement date.

[Outgoing camt.087](#)

The user can perform the following on an outgoing camt.087 message:

- Initiate a camt.087 message from the provided enquiry. The enquiry lists all the outgoing pacs.008 messages in completed status, which has been sent to clearing.
- While initiating the camt.087 message from the enquiry, the system checks whether the camt.087 request is initiated within 13 months of the original credit transfer or not. If the camt.087 request is initiated outside the parameterised timeframe, then an error message is displayed and user is not allowed to initiate the camt.087 message.
- The modified interbank settlement date field is defaulted with original credit value date of outgoing pacs.008 message.
- If there is no change in the modified interbank settlement date, the Instruction for Assignee code and Instruction Information for Assignee becomes mandatory.
- If the user changes the date in modified interbank settlement field to a new date, the Instruction for Assignee code and Instruction Information for Assignee becomes non-mandatory.
- The status of camt.087 message is updated to claim sent status in TPH.
- Outgoing camt.027 message is generated in the outgoing message folder.

[Incoming camt.087](#)

The system performs the following when a camt.087 message is received by the beneficiary bank.

- The incoming camt.087 message is processed and uploaded.
- Enquiry is provided to the user to view the incoming camt.087 message.
- The system matches the incoming camt.087 message with the original pacs.008 message, which was already processed.
- If the original payment is not found, the system updates the Enquiries for Questions and Answers (EBQA) status with UNMATCHED.
- If the original payment is found, the system checks whether the camt.087 message is received within the acceptance days. If it is true, the system proceeds processing (STP) the camt.087 message, else the incoming camt.087 message is parked for manual intervention.
- If the original payment is found and is within the acceptance days, the system checks whether the original payment is in completed status. If it is true, the system proceeds processing (STP) the camt.087 message, else the incoming camt.087 message status is updated as invalid claim. The claim is invalid because the original payment could have been returned already and there is no possibility to modify the date in the original payment, hence no manual action can be taken if the claim is set as invalid.
- If the original payment is in completed status and automated return indicator is set to YES, the system checks whether the modified date and the original credit value date of the pacs.008 transaction are same.
  - If the dates are not same, the camt.087 request is parked for manual action and status is updated to INWORK.
  - If the dates are same, the camt.029 message is generated automatically with the RJVA status.

## Processing of Cash Management Receipt (camt.025.001.03)

Temenos Payments Hub handles cash management receipt (camt.025 ACCP and camt.025 RJCT) received as an acknowledgment from EUROSIC clearing for the outward messages such as camt.027, camt.087, camt.056 and camt.029.

If negative cash management is received, that is camt.025 RJCT, Temenos Payments Hub marks the underlying camt message as clearing rejected, else there is no change in the original camt message until camt.029v3 or camt.029v8 response is received from the beneficiary bank.

## SWIFT gpi and UETR Support

The gpi Service Type Identifier and Unique End-to-End Transaction Reference (UETR) received in the following MT type messages are mapped to the EUROSIC ISO message format.

Gpi-enabled messages can be processed for pacs.008 (payment types 'CSTPMT') customer payments and for pacs.009 (F2FPMT and COVPMT payment types) bank payments.

- MT103 Single Customer Credit Transfer
- MT202COV General Financial Institution Transfer

The <InstrId> tag in pacs.008 or pacs.009 message is to identify a gpi-enabled message (service type identifier) and to carry UETR.

UETR as 32!x (Formatted using IETF’s RFC 4122 v4 lower case without hyphens).

Internet Engineering Task Force (IETF) was established in 1986 to coordinate the operation, management and evolution of the internet. Request for Comments (RFC) is an internet standard.

[Formatting Specifications](#)

Service type identifier = G01

UETR (32!x) = eb6305c91f7f49deaed016487c27b42d

| MT103 / MT202COV | ISO 20022 - pacs.008 / pacs.009 |
| --- | --- |
| Header - field 111 - 3!n Service type identifier [001] | InstrId  For example, <InstrId> G01eb6305c91f7f49deaed016487c27b42d <\InstrId> |

## Support to pacs.009COV

Temenos Payments Hub supports the below features for pacs.009COV when received or sent through EUROSIC clearing.

- Initiating an outgoing MT103 with cover sent as pacs.009COV.
- Receiving and processing of 202COV which is redirected as pacs.009COV through EUROSIC.
- Receiving and processing inward pacs.009COV from EUROSIC for an inward pacs.008 or MT103 with beneficiary having an account in the books of the processing bank (TPH).
- Receiving and processing of pacs.009COV, which is redirected as MT202COV through SWIFT.

## Generate or Process Payment Status Report (pacs.002)

As a response to inward EUROSIC credit transfer payment, Temenos Payments Hub generates pacs.002 (positive or negative) message as an acknowledgment to clearing. Temenos Payments Hub must process the pacs.002 (ACCP or RJCT) received from EUROSIC clearing for an outward EUROSIC credit transfer validation.

The originator bank can receive or send pacs.002 clearing status report for the EUROSIC credit transfer messages (pacs.008, pacs.009, pacs.004, and pacs.028).The clearing status report received from the clearing can be processed Straight-Through Processing (STP) or Non-STP.

## SIC and EuroSIC Rulebook for Customer Credit Transfer pacs.008

This functionality allows banks to support SIC and EuroSIC clearing functionality with the latest upto date rulebook changes published for 2023 respectively enhancing the pacs.008 incoming and outgoing message with the latest changes.

This SIC and EuroSIC clearing functionality offered to any new client will have the latest rulebook changes updated for quicker implementation without any gaps.

As part of SIC and EuroSIC RB 23 changes, LEI added as an option for organisation identification to SEPPMT for Ultimate Debtor, Debtor, Creditor and Ultimate Creditor.

## SIC and EuroSIC Rulebook for Customer Credit Transfer camt.027

This functionality allows banks to support the EuroSIC clearing functionality with the latest up to date rulebook changes published for 2023, respectively enhancing the camt.027 message.

As part of the rulebook 2023, mapping and functional changes are added for the camt.027 message.

The following new elements are added to:

- Assignment>Assigner>Agent>Financial Institution Identification>Other
- Assignment>Assigner>Agent>Financial Institution Identification>Other Identification
- Assignment>Assignee>Agent>Financial Institution Identification>Other
- Assignment>Assignee>Agent>Financial Institution Identification>Other Identification
- Underlying>Interbank>OriginalUETR
- Underlying>Interbank>OriginalTransactionReference

## SIC and EuroSIC Rulebook for Bank Credit Transfer for pacs.009 and pacs.004

This functionality allows banks to support SIC and EuroSIC clearing functionality with the latest up to date rulebook changes published for 2023 respectively enhancing the pacs.009 and pacs.004 messages with latest changes.

For pacs.009, as part of the rulebook 2023 changes BXDSTM is added to third party system payment type. The existing SIC and EuroSIC bank transfer PO version has been enhanced as per rulebook 2023 changes. The third party system payment type BXDSTM has been added in the PO version in payment type. The following have been considered:

- Participant banks will allow initiation of bank transfer payment (pacs.009) for third party system payment type BXDSTM.
- Addition in payment type (BXDSTM) has resulted in mapping changes for the below mentioned tags:

  Transaction Identification, Local Instrument proprietary , Settlement Priority ,Settlement Time request ,Previous Instructing Agent 1, 2 and 3 ,Previous Instructing Agent 1, 2 and 3 account , Intermediary Agent 1, 2 and 3 ,Intermediary Agent 1, 2 and 3 account ,Debtor (LEI ,Name and Postal address) ,Debtor account ,Debtor Agent ,Debtor Agent account ,Creditor Agent ,Creditor Agent account ,Creditor (LEI ,Name and Postal address ), Creditor account ,Instruction Information ,Remittance Information ,Remittance Information ,Underlying Customer Credit Transfer.

For pacs.004, LEI option has been enabled only for SEPRTN. The AddtlnInf will be sent with ATR053 and ATR072 instead of AT-51 and AT-R7 for respective recall messages.

- In the case of a *"Positive Response to a Recall of SEPA Credit Transfer Dataset (DS-06)”* message: must be present, starting with "ATR053/" followed by the information as per attribute description *“The specific reference of the Originator PSP initiating the Recall (AT-R053)”*.
- In the case of a *"Positive Response to the Request for Recall by the Originator Dataset (DS-08)"* message: must be present, starting with "ATR072/" followed by the information as per attribute description *"The specific reference of the Originator PSP for the Request for Recall by the Originator (AT-R072)"*.

  Validation has been removal for Structured address i.e., Under structured address town name and country is not mandatory for Debtor, Creditor, Ultimate Debtor and Ultimate Creditor .

## SIC and EuroSIC Rulebook for camt.025, camt.029 and camt.056

This functionality allows banks to support SIC and EuroSIC clearing functionality with the latest up to date rulebook changes published for 2023 respectively enhancing the camt.025, camt.029 and camt.056 messages.

Changes have been performed in the *Original Message Name Identification* tag for camt.025, as follows: Message type presentation changed, Additional digits to indicate the complete message version (e.g. "camt.025.001.07") are permitted but will not be validated by the RTGS system.

## SIC and EuroSIC Rulebook for camt.087

This functionality allows banks to support EuroSIC clearing functionality with the latest upto date rulebook changes published for 2023 respectively enhancing the camt.087 message. Mapping and functional changes are added as part of the rulebook 2023 changes.

The following new elements are added to:

- Assignment>Assigner>Agent>Financial Institution Identification>Other
- Assignment>Assigner>Agent>Financial Institution Identification>Other Identification
- Underlying>Interbank>OriginalUETR
- Underlying>Interbank>OriginalTransactionReference

## SIC and EuroSIC Rulebook for camt.029 (SEPA) and pacs.028

This functionality allows banks to support SICand EuroSIC clearing functionality with the latest upto date rulebook changes published for 2023, respectively enhancing the pacs.028 message.

For the camt.029 (SEPA) message, the following mapping and functional changes are added as part of the rulebook 2023 changes:

- New elements are added to:
  - Assignment>Assigner>>Agent>>>Financial Institution Identification>>>>Clearing System Member Identification
  - Assignment>Assigner>>Agent>>>Financial Institution Identification>>>>Other
  - Assignment>Assigner>>Agent>>>Financial Institution Identification>>>Other>>>>Identification
  - Assignment>Assignee>>Agent>>>Financial Institution Identification>>>>Clearing System Member Identification
  - Cancellation details
- Cardinality change in:
  - Resolved case from 1..1>0..1
  - Modification details from 1..1 > 0..1
  - Resolution Related Information>Compensation>>Creditor Agent>>>Financial Institution Identification>>>>Other from 0…1>1..1
  - Resolution Related Information>Charges>>Agent>>>Financial institution identification>>>>Other from 0…1 > 1..1
- Sub element Original next agent has been removed from the claim non receipt details>Accepted

For the pacs.028 (SIC and EuroSIC) message, the following mapping and functional changes are added as part of the rulebook 2023 changes:

- New elements are added:
  - Original Group Information
  - Original Group Information>>Original Message Identification
  - Original UETR
  - Acceptance Date and time (Must not be used within SIC/euroSIC (exclusively intended for use in the context of instant payments).
  - Clearing System Reference
  - Instructing Agent>>Financial Institution Identification>>>Clearing System Member Identification
  - Instructing Agent>>Financial Institution Identification>>>Other
  - Instructing Agent>>Financial Institution Identification>>>Other>>>>Identification
  - Instructed Agent>>Financial Institution Identification>>>Clearing System Member Identification
  - Original Transaction Reference>Debtor Agent Account
  - Original Transaction Reference>Creditor Agent Account
  - Original Transaction Reference>Creditor Agent Account
  - Original Transaction Reference>Purpose
- Movement of elements from A-C: Elements Instg Agt and Instd Agt are moved from A-C level
- Cardinality change in:
  - Original Instruction Identification from 1..1->0..1
  - Original End To End Identification from 1..1->0..1
  - Original Transaction Reference 1..1->0..1

## Amount Split for Transfer above EUR 50 Million for Payment Messages

This functionality allows banks to generate outgoing split messages for pacs.008, pacs.009, camt.056, pacs.028 and receive incoming pacs.008, pacs.009, pacs.004, camt.056, pacs.028 for the split amount. All R transactions that are received will be manually handled.

For processing the outgoing pacs.008, pacs.009 for payments greater than EUR 50 million, an API will be attached in the Enrich Out Message API of the `PP.CLEARING` > SIC record to split the payment messages (i.e. multiple IF events) for pacs.008, pacs.009, camt.056, pacs.028 and only maximum of EUR 50 million will be present in each split message. Also, mapping level changes have been added of transaction reference for outgoing pacs.008, POA and channel validations.

In case of incoming pacs.008 and pacs.009 > EUR 50 million, these will be received as already split messages (As sent by the initiator), so no separate processing is required in TPH and each message will be booked separately.

To process the outgoing cancellation requests (camt.056), it will be initiated a camt.056 request using the **Payments > Payment Hub > Payment Investigations and Cancellations > Cancellations > RTGS Cancellations > Create RTGS Cancellation Requests > Customer Initiated Cancellation Request / Bank Initiated Cancellation Request** menu. A cancellation request camt.056 can be initiated for the original outgoing transaction for pacs.008 or pacs.009 based on the single `POR.TRANSACTION` but the Enrich Out Message API split the payment into multiple camt.056 messages if the local reference field, *SplitPayment* in `POR.SUPPLEMENTARY.INFO` for that transaction is set as Yes.

The incoming cancellation request (camt.056) will be composed of one message per split message received initially. So responses can thus be individual for each message. This might lead to a mix of camt.029 and pacs.004 sent out, but as the original transaction was booked according to the split messages (not the whole amount). So it will be treated like any other normal EUROSIC payment message.

When processing of outward pacs.028, the status request message pacs.028 can be initiated for the outgoing cancellation message camt.056 based on the single `POR.TRANSACTION` but the Enrich Out Message API split the payment into multiple pacs.028 messages if the local reference field, *SplitPayment* in `POR.SUPPLEMENTARY.INFO` for that transaction is set as Yes.

An incoming status request (pacs.028) will be composed of one message per split message received initially, so responses can thus be individual for each message and it will be treated like any other normal EUROSIC payment message.

When we receive a pacs.002 from EUROSIC for an outward pacs.008, pacs.009 or pacs.028 sent, then pacs.002 is expected to go to the Unmatched queue for manual handling.

To handle the generation of pacs.028 (SIC), the status request message pacs.028 can be initiated for the outgoing cancellation message camt.056 based on the single `POR.TRANSACTION` but the Enrich Out Message API split the payment into multiple pacs.028 messages if the local reference field, *SplitPayment* in `POR.SUPPLEMENTARY.INFO` for that transaction is set as Yes.

For processing of incoming status requests pacs.028 (SIC), the incoming status request (pacs.028) will be composed of one message per split message received initially, so responses can thus be individual for each message and it will be treated like any other normal sic payment message.

When a pacs.002 from SIC is received for an outward pacs.028 sent, then pacs.002 is expected to go to the Unmatched queue for manual handling.

In this topic

- [Introduction to Euro Swiss Interbank Clearing (EUROSIC)](#IntroductiontoEuroSwissInterbankClearingEUROSIC)

- [Type of Participant](#TypeofParticipant)
- [Type of Payment and Message](#TypeofPaymentandMessage)
- [Payment Instruments](#PaymentInstruments)
- [Identifiers](#Identifiers)
- [Initiating Customer Credit Transfers](#InitiatingCustomerCreditTransfers)
- [Receiving Incoming Credit Transfer (pacs.008.001.002 or pacs.009.001.02)](#ReceivingIncomingCreditTransferpacs008001002orpacs00900102)
- [Returning EUROSIC Credit Transfers (pacs.004.001.002)](#ReturningEUROSICCreditTransferspacs004001002)
- [Recalling Settled Credit Transfer (camt.056.001.01)](#RecallingSettledCreditTransfercamt05600101)
- [Request Status Update (pacs.028.001.01)](#RequestStatusUpdatepacs02800101)
- [Claim of Non-receipt by Originator (camt.027.001.06)](#ClaimofNonreceiptbyOriginatorcamt02700106)
- [Claim Value Date Correction or Request to Modify Payment (camt.087.001.05)](#ClaimValueDateCorrectionorRequesttoModifyPaymentcamt08700105)
- [Processing of Cash Management Receipt (camt.025.001.03)](#ProcessingofCashManagementReceiptcamt02500103)
- [SWIFT gpi and UETR Support](#SWIFTgpiandUETRSupport)
- [Support to pacs.009COV](#Supporttopacs009COV)
- [Generate or Process Payment Status Report (pacs.002)](#GenerateorProcessPaymentStatusReportpacs002)
- [SIC and EuroSIC Rulebook for Customer Credit Transfer pacs.008](#SICandEuroSICRulebookforCustomerCreditTransferpacs008)
- [SIC and EuroSIC Rulebook for Customer Credit Transfer camt.027](#SICandEuroSICRulebookforCustomerCreditTransfercamt027)
- [SIC and EuroSIC Rulebook for Bank Credit Transfer for pacs.009 and pacs.004](#SICandEuroSICRulebookforBankCreditTransferforpacs009andpacs004)
- [SIC and EuroSIC Rulebook for camt.025, camt.029 and camt.056](#SICandEuroSICRulebookforcamt025camt029andcamt056)
- [SIC and EuroSIC Rulebook for camt.087](#SICandEuroSICRulebookforcamt087)
- [SIC and EuroSIC Rulebook for camt.029 (SEPA) and pacs.028](#SICandEuroSICRulebookforcamt029SEPAandpacs028)
- [Amount Split for Transfer above EUR 50 Million for Payment Messages](#AmountSplitforTransferaboveEUR50MillionforPaymentMessages)

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
Tuesday, April 14, 2026 4:21:06 PM IST