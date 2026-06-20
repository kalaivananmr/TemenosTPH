# Introduction to Swiss Interbank Clearing (SIC)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
    - [Introduction](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
    - [Configuration](../../Europe/Europe_Swiss_Clearing_PPSICH/Configuration.htm)
    - [Working with](../../Europe/Europe_Swiss_Clearing_PPSICH/Working_with.htm)
    - [Tasks](../../Europe/Europe_Swiss_Clearing_PPSICH/Tasks.htm)
    - [Outputs](../../Europe/Europe_Swiss_Clearing_PPSICH/Outputs.htm)
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

Updated On 20 January 2026 |
 86 Min(s) read

Feedback
Summarize

# Introduction to Swiss Interbank Clearing (SIC)

Swiss Interbank Clearing (SIC) is the electronic central Swiss Payment system. The participating financial institutions process their large value payments as part of their retail payments in Swiss Francs (CHF). Swiss National Bank (SNB) conducts the SIC clearing (which is an RTGS system, where each payment is settled individually and permanently). SIC participants have their sight deposit accounts at the Swiss National Bank (SNB), which serve as a means of payment. The messages used are according to the ISO standards with SIC rule book specifications.

[SIC Payments](#)



| Bank’s STP Channels | TPH’s own bank electronic channels or aggregators |
| --- | --- |
| Ordering Banks | A partner bank of TPH bank sending payment instructions to be cleared with SIC RTGS. |
| Payment Order | Front end Temenos Transact module to manually capture SIC payments or receive payment instructions from customer channels. |
| Payment Engine | Payment system from TPH to process the payments. |
| IIB | Middleware used by TPH to interact with the SIC RTGS system. |
| SIX | SIC RTGS system. |
| AML | Bank’s Anti-Money Laundering or Fraud Check system. |
| cTemenos Transact or External DDA | Bank’s core banking system. |

[Types of SIC Payment Messages](#)

Temenos Payments Hub supports the following types of SIC Payment Messages:

| Message Type | Description |
| --- | --- |
| pacs.008.001.08.ch.02 | Customer Payments |
| pacs.009.001.08.ch.02 | Bank and Third-party System Payments |
| pacs.002.001.10.ch.02 | Payment Receipts |
| pacs.004.001.09.ch.02 | Payment Returns |
| camt.025.001.05.ch.01 | Cash Management Receipts |
| camt.056.001.08.ch.02 | Return Request |
| camt.029.001.09.ch.01 | Return Request Rejection |

[SIC Participants](#)

TPH is configured to act as SIC direct participant according to SIC message compliances. However, SWIFT messages from other banks can be redirected to SIC Clearing through the direct participant.

SIC does not have indirect participants.

[Types of SIC Payments](#)

SIC has certain payment types to define transfer that is done (for example, customer payments, salary payments, etc). These payment types determine the format of every SIC message, and is received in *Local Instrument Proprietary* field. The following are the payment types for customer and bank transfers:

[Customer Transfers](#)

| Payment Type | Description |
| --- | --- |
| ESRDEB | LSV payment resulting from a Direct Debit (DD) |
| IPIDEB | IPI payment resulting from a DD |
| CSTPMT | Generic customer payment |

[Bank Transfers](#)

| Payment Type | Description |
| --- | --- |
| F2FPMT | FI to FI payment |
| CMPPMT | Compensation payment |
| COVPMT | Cover payment |
| PPTTSD | Sight deposit account transfer by participant |
| SECSTM | SECOM settlement |
| EUXSTM | Eurex settlement |
| REPSTM | Repo settlement |
| BCMSTM | Bancomat settlement |
| POSSTM | EFT or POS settlement |
| STVSTM | Terravis settlement |
| VISSTM | Viseca settlement |
| BX Digital Settlement | BXDSTM |

[SIC Payment Message Flow](#)



[](#)[Duplicate Check](#)

TPH performs the SIC payment duplicate check at two levels for incoming messages:

- Message (File) level
- Payment (Transaction) level

These two checks are independent of each other, and are configured at the product condition level.

Duplicate check is applicable for incoming SIC messages, such as pacs.008, pacs.009 and pacs.004.

[Clearing Directory and Reachability](#)

TPH supports loading of the SIC Clearing Directory and reachability check. Reachability for SIC payments is based on BIC. SIC payment specific reachability API is available in TPH to perform the reachability check according to the clearing rules.

[Clearing Cut-Off](#)

The clearing cut-off for SIC RTGS payments is 6:00PM (CET) settled on the same value date. If breached, the payments are settled on the next value date.

[Warehouse](#)

Warehousing is done for SIC transactions according to the standard warehouse functionality of TPH for future dated payments. If the participant enters:

- All the payments by 5PM (Clearing Cut-off 1), it is settled and processed on the same value date.
- Customer payments after 5PM, it is settled on the next value date.

These payments are warehoused until the next value date.

[Manual Entry](#)

The payment order page is available for Customer and Bank Transfer each. It allows the bank’s user to manually enter the SIC RTGS payments. Additionally, to perform payment type validations for the SIC payments. To know more, refer to the [Working with](Working_with.htm#top) section .

[Return and Repair](#)

The return and repair details are provided below.

[TPH as Beneficiary Bank](#)

If there is an issue in processing the inward payment for example, when the beneficiary account is invalid, TPH automatically returns the funds. A return payment (that is pacs.004) is sent to SIC and the system marks the original payment as ’Completed with Return’. Additionally, the payment is parked for manual repair (if configured), and the user can manually return or reject the payment. Returns are applicable for both complete and incomplete (payment in repair queue) payments.

[TPH as Originating Bank](#)

If a negative confirmation is received for pacs.008 or pacs.009 or pacs.009 COV that is sent to SIC, the payment is moved to an exception (Repair) queue in TPH for manual handling. TPH can also receive return from SWIFT for original redirected Bank transfer received from the clearing.

Returns are applicable for both complete and incomplete (payment in repair queue) payments. If return is initiated by bank, then the company BIC is populated but when return is originated by customer then the debtor’s name along with postal address (optional) is populated.

[Rejects from SIC](#)

If a return is received for pacs.008 or pacs.009 that is sent to SIC, the payment is moved to an exception (Repair) queue in TPH for manual handling.

[Outward Processing](#)

The below section describes the outward processing of a payment sent to SIC Clearing.



| Activity | Description |
| --- | --- |
| Manual capture of SIC payments from branch or back-office using `PO` application | - Captures a SIC payment from the `PO` application. - Validates mandatory (such as payment type) and non-mandatory fields on submission and displays an error (if any). |
| Payment instructions using ordering bank | Sends SIC payment instructions to TPH bank. The instruction can be in SWIFT MT (MT 103 or 202) or any ISO20022 format. |
| Account validations | Validates whether ordering or debit account:  - Is a valid Temenos Transact account - Has no posting restrictions - Has sufficient balance to be reserved to cover the transaction |
| Bank code validations | Validates the beneficiary bank code (BIC or BC number) against the SIC directory.  - If this directory is loaded, the system is configured to validate bank code. |
| Business validations | Instructed amount needs to be empty. If provided, the currency needs to be CHF.  Transaction currency needs be equal to CHF. |
| Reachability check | `PO` application validates whether the beneficiary bank (BIC or BC) is reachable directly (if configured). |
| Submission and supervisor approval | After submission of the payment, the process is as follows:  - It awaits supervisor’s approval. - Once approved, it is moved for further processing - It is sent to Temenos Payments Hub Engine.   Payments received in TPH from external banks using STP mode, do not await supervisor’s approval. |
| Warehouse | Warehouses payments with future execution date. It is released on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank specific requirement that is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (SIC), which determines the message type (pacs.008 or pacs.009). If the system finds that the clearing cut-off has crossed for SIC, the payment is routed using an alternate channel. If configured or warehoused by TPH, the payment is released on the next business day. Routing is done using an alternate channel that is available only with PH license. |
| Dates calculation | Calculates the payment value and booking date, which isconfigured to current date (same as execution date). |
| FX calculation | Applies when the customer and payment account currency are different. If any FX shifts are involved, it adjusts the value date forward and warehouses the payment.  This feature is only supported with PH license. |
| Balance reservation | Reserves funds on the debit account. Balance reservation is done on payment amount along with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, then it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges for the SIC payments (if configured). |
| Duplicate check | Performs at message or file level for the SIC payments received from ordering bank or channels. To know more on criteria, refer to [Duplicate Check](#Duplicate_Check) section. |
| Posting | Debtor’s account is debited with payment amount and charges (if any) are borne by the customer. If posting fails due to insufficient funds, it holds the payment in Repair queue for user action (Automatic Retry, Reject or Cancel).  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, then it generates posting request in a native XML format and accepts response from the external system.  Outward Payments Following are the entries made before sending pacs.008 or pacs.009 to SIC:  - Debit debtor account (Ordering customer or bank account) - Credit SIC clearing nostro account  When the pacs.004 is sent:  - Dr SIC return suspense account - Cr SIC clearing account  Settlement Booking Entry  - When SIC payments are processed, the clearing Nostro is directly credited or debited. - There is no separate settlement processing, therefore, no settlement accounting for SIC payments. |
| SIC channel validations | Performs all SIC specific validations on the payment to ensure that the payment meets the compliance requirements of SIC. |
| Error queue | If an error occurs (when SIC payment is a processed STP), it moves the transaction to the Repair queue for the user to repair or cancel the payment. |
| Outward cover processing | Supports capturing an outgoing international customer payment with cover. It determines the cover method of routing based on product and routing configuration. If the cover channel is determined as SIC, the system generates pacs.009 Cover message and sends it to SIC. |

[Inward Processing](#)

The below section describes the inward processing of a payment received from SIC clearing.



| Activity | Description |
| --- | --- |
| SIC payment received from Clearing | Receives the inward payment pacs.008 or pacs.009 in TPH from SIC clearing. |
| Processing a cover payment | TPH receives a cover payment in pacs.009 format from SIC. It identifies the payment as a cover and invokes the hold for cover functionality. Additionally, it interacts with `AC.EXPECTED.RECS` application to match the cover payment with the underlying transaction and releases it for further processing. |
| SIC specific format validations | Performs SIC specific validations on the payment. |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary bank BC number or account number unknown - Beneficiary account closed - Beneficiary account stopped - Account is not in the quoted currency |
| Bank code validation | Validates creditor BIC or BC number. |
| Dates calculation | Receives SIC payments with value date as current business date and processes the payment immediately. |
| Filtering | Performs payment filtering when configured. This is a bank specific requirement and is performed in the site. |
| Fee calculation | Charges are taken (if configured) in TPH for SIC Payments.  This is applicable only for customer transfers. |
| Duplicate check | Performs the check on payments received from SIC payments for the configured set of payment attributes. The SIC payment duplicate check is at the message and transaction level. |
| Credit posting | Debits the SIC Clearing Nostro account and posts the credit to the beneficiary account.  - Debit SIC Clearing Nostro account - Credit customer account |
| Error queue | If an error occurs while processing the SIC payments, it moves the transaction to the Repair queue for the user to repair or return the payment. |

## Amount Split for Transfer above CHF 100 Million

According to SIC clearing, when transactions between SIC participants exceed CHF 100 million, it is split into individual transaction of CHF 100 million each. This allows to configure the system as follows:

- Generate split messages for outgoing messages (pacs.008, pacs.009, and camt.056)
- Handle incoming messages as individual transactions
- Handle R-message requests (camt.029, pacs.002 and pacs.004). For example, a cancellation request (camt.056) can be initiated for the original outgoing transaction (pacs.008 or pacs.009) based on the single `POR.TRANSACTION`. This splits the payment into multiple camt.056 messages based *SplitPayment* flag in `POR.SUPPLEMENTARY.INFO`.

## Receive camt.025 with ACCP or RJCT Status

The clearing receives a camt.025 message, when business validation for the outgoing camt.029 or camt.056 message fails or is successful.

- If the <StsCd> tag in the camt.025 has the value ‘ACCP’, the outgoing camt.056 or camt.029 is accepted by the clearing.
- If the <StsCd> tag in the camt.025 has the value ‘RJCT’, the outgoing camt.056 or camt.029 is rejected by the clearing.

## Category Purpose

The category purpose specifies the high-level purpose of the payment instruction based on a set of pre-defined categories. The category purpose can be provided in coded or proprietary form. This is an optional information.

When the coded form is used, the code should be a valid one as per the ExternalCategoryPurpose1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets).

When the user captures the payment using the PO application or OE screen, dropdown fields, the list of category purpose codes are provided. The user can select the appropriate category purpose code from the dropdown. A separate validation is not done on the applicable codes.

When this field is received in an incoming message, the category purpose details are stored in the system as code words:

- Information code = INSBNK.
- Code word = CYPURPCD (code) or CYPURPPY (proprietary).
- Code word text = <the code or proprietary value received>.

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

For the payment type CMPPMT, the category purpose code or proprietary is mandatory.

## Instruction for Next Agent

Specifies further information related to processing of the payment instruction, which may need to be acted upon by the next agent. This is an optional information consisting of only textual information (no code).

A maximum four occurrences of Instruction for Next agent is mapped.

When the user captures a payment using the PO application or OE screen, dropdown fields, the list of instruction codes are provided. The user can select the appropriate instruction code from the dropdown and enter additional information.

When this field is received in an incoming message, the instruction for next agent details are stored as mentioned below (even though it does not have a code):

- Information code = INSSDR.
- Code word = NULL (no value).
- Code word text = <received instruction information>.

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment the received information is passed if configured for outbound code word generation.

## Remittance Information

Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system. Remittance Information is optional. unstructured remittance information, it is mandatory to provide the value.

## Service Level

This indicates the agreement under which or rules under which the transaction should be processed. Service level can be provided as a code or in a proprietary form.

When coded form is used, the code should be a valid one as per ExternalServiceLevel1Code list. This information is available at External code sets | ISO20022.

When the user captures the payment using PO application or OE screen, dropdown fields lists the service level codes. The user can select the appropriate service level code from the dropdown. No separate validation is done on the applicable codes.

When this field is received in an incoming message, the service level details are stored in the system like code word, as follows:

- Information code = INSBNK.
- Code word = SVCLVL (code) or SVCLVLPY (proprietary).
- Code word text = <the code or proprietary value received>.

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

## Time Indication

The user can provide information on the requested settlement time(s) of the payment instruction. The system supports to capture the following settlement time indication fields and sends in the generated message.

The user should enter the data in the time indication value fields using format HH:MM:SS+/-hh:mm (where, HH – hour, MM – minute, SS – second, +/- hh:mm indicates offset in hour and minute).

The user should enter the offset while capturing the details, otherwise the system considers offset as +00:00.

If time is entered as HH:MM+/-hh:mm, the system considers the time as HH:MM:00+/-hh:mm and processes further.

If time is entered as HH:MM, then the system consider the time as hh:mm:00+00:00 and processes further.

If time is entered as HH:MM+/-, then the system consider the time as hh:mm:00+/-00:00 and processes further.

When this field is received in an incoming message, the time settlement and time indication fields are stored in the system as code words:

- Information code = TIMIND.
- Code word = CLSTIME or TILLTIME or FROMTIME or RJCTTIME.
- Code word text = <time value received>.

There is no specific validation or processing done in system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed as received if configured for outbound code word generation.

The system supports the following fields in the *Time Indication Type* field:

| Value | Description |
| --- | --- |
| CLSTIME | This is the clearing and settlement time. |
| FROMTIME | The time from which the settlement happens in clearing |
| TILLTIME | The time until which the payment can be settled in clearing |
| RJCTTIME | If the payment is not settled within this time, clearing should reject the payment |

For SIC Bank, the *Transfers Settlement Time Indicator* field is applicable only for payment types F2FPMT and COVPMT.

## Message Priority

Message priority is an indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction. Allowed values are:

| Value | Description |
| --- | --- |
| NORM | Indicates that the priority level is normal |
| HIGH | Indicates that the priority level is high |

## Regulatory Reporting

Specifies the information required for regulatory and statutory requirements. This is an optional information.

While the user initiates a payment using the PO application or OE screen, the system supports capturing regulatory information which comprises of the following:

- *Debit Credit Reporting Indicator:* This is a coded information which identifies whether the regulatory information applies to debit side, credit side, or both side of the transaction. Allowed values are:
  - BOTH: Regulatory information applies to both credit and debit sides.
  - CRED: Regulatory information applies to the credit side.
  - DEBT: Regulatory information applies to the debit side.
- *Authority*: Indicates the entity that requires the regulatory reporting information.
- *Name*.
- *Country*.
- *Details*: Provides details on the regulatory reporting information. Multiple occurrences are allowed. It consists of the following fields:
  - Type.
  - Date.
  - Country.
  - Code.
  - Amount.
  - *Information* (multiple occurrence).

When an incoming payment is received with regulatory reporting information, the details are stored in the system. If the payment is redirected, the received regulatory reporting information is passed unchanged.

There is no specific validation or processing done in the system for this information.

## Inward camt.025 Processing for Outward Messages

This functionality allows banks to manage the incoming camt.025 messages as part of the SIC 2022 rulebook changes, to adapt the CBPR+ usage.

New functionality and mapping level changes have been released to support the incoming camt.025 messages.

## QR Billing for SIC and euroSIC Clearing

In the past, several different payment slips have been used in Switzerland to transfer money to the recipient’s account. The introduction of the QR bill in June 2020 was one of the steps to make payments digital and modernize Swiss payment transactions. The QR bill contains a QR code and can be printed or issued digitally. All payment information is contained both digitally in the Swiss QR code and plain text.

For the payment part of the QR bill to work successfully, payments are handled using a structured reference, based on a special IBAN, the QR IBAN or a structured creditor reference. In principle, the QR code payment part is designed for payments in Switzerland and Liechtenstein, not for foreign payment transactions. However, there are cases where a QR payment is sent through the SEPA channel or even SWIFT if marked respectively.

QR IBAN can be identified with the check digit code (SIC Id) starts with range of 30000 – 31999. FOR QR payment, Under structured Remittance information , proprietary tag should contain QRR.

QR transactions can be received through a pain.001 message or can be manually entered via POA version or TPH Order Entry screen by the operations staff.

There are three different distinctions of the QR bill:

- Distinction 1: QR-bill containing a QR-Reference (QRR) and a QR-IBAN. This is always a domestic payment and must be sent either through SIC or euroSIC.
- Distinction 2: QR-bill containing a Customer Reference (SCOR) and a regular IBAN. This can be a domestic or a cross-border payment and can be sent through any of the modules.
- Distinction 3: QR-bill containing no reference but a regular IBAN. This can be a domestic or cross-border payment and can be sent through any of the modules.

TPH supports the processing of incoming QR bill payments (pain.001), initiation of QR bill payments via the Payment Order Application (POA) or Order Entry (OE) and generation of the outgoing pacs.008 message for SIC and euroSIC.

## LSV Direct Debit

In Switzerland, a standard direct debit order is referred to as a Lastschrift Verfahren (LSV). The LSV+ direct debit is an improved version of LSV that allows companies to retrieve payments directly from their customer’s bank accounts.

Thus, the LSV+ direct debit offers the debtor the right of objection. In LSV+, the debtor can object to a payment made at his or her financial institution, without having to provide a reason for doing so, up to 30 days after notice of the debit to the account has been given.

This functionality allows banks to manage SIC and EuroSIC Lastschrift Verfahren (LSV) direct debit payments in TPH, to receive pain.001.001.03 messages, process and generate the outgoing pacs.008 messages.

New functionality and mapping level changes have been released to support the processing of LSV direct debit payments for SIC and EuroSIC.

Using this functionality, bank users are able to resubmit or cancel transactions from the repair queue, in case of an invalid IPI reference. Temenos Payments Hub will check if all the mandatory elements are received and stored in the system and will move the payment to the repair queue if any of the values do not match the validation criteria. Also, bank users will be able to receive and validate the D10 messages, cancel and process the return payments.

LSV Direct Debit functionality supports receiving for pain.001 or D10 message from clearing with 5 digit CHBCC code, which is replaced with 6 digit CHSIC code. As part of this enhancement, we support receiving LSV DD request (pain.001 or D10) with 3 to 5 digit CHBCC code which is replaced with 6 digit CHSIC code in the outgoing pacs.008 message.

## Illustrating Model Parameters

To know more on parameter setup for SIC, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

SIC module can send and receive the real time gross settlement payments used in the Switzerland.

## SIC and EuroSIC Rulebook for Bank Credit Transfer for pacs.009

This functionality allows banks to support SIC and EuroSIC clearing functionality with the latest up to date rulebook changes published for 2023 respectively enhancing the pacs.009 message with latest changes.

For pacs.009, as part of the rulebook 2023 changes BXDSTM is added to third party system payment type. The existing SIC and EuroSIC bank transfer PO version has been enhanced as per rulebook 2023 changes. The third party system payment type BXDSTM has been added in the PO version in payment type. The following have been considered:

- Participant banks will allow initiation of bank transfer payment (pacs.009) for third party system payment type BXDSTM.
- Addition in payment type (BXDSTM) has resulted in mapping changes for the below mentioned tags:

  Transaction Identification, Local Instrument proprietary , Settlement Priority ,Settlement Time request ,Previous Instructing Agent 1, 2 and 3 ,Previous Instructing Agent 1, 2 and 3 account , Intermediary Agent 1, 2 and 3 ,Intermediary Agent 1, 2 and 3 account ,Debtor (LEI ,Name and Postal address) ,Debtor account ,Debtor Agent ,Debtor Agent account ,Creditor Agent ,Creditor Agent account ,Creditor (LEI ,Name and Postal address ), Creditor account ,Instruction Information ,Remittance Information ,Remittance Information ,Underlying Customer Credit Transfer.

## SIC and EuroSIC Rulebook for camt.025, camt.029 and camt.056

This functionality allows banks to support SIC and EuroSIC clearing functionality with the latest up to date rulebook changes published for 2023 respectively enhancing the camt.025, camt.029 and camt.056 messages.

Changes have been performed in the *Original Message Name Identification* tag for camt.025, as follows: Message type presentation changed, Additional digits to indicate the complete message version (e.g. "camt.025.001.07") are permitted but will not be validated by the RTGS system.

For camt.029, the changes in code values due to revised SEPA attributes, have been performed, as fiollows:

- CxlDtls/TxInfAndSts/CxlStsRsnInf/AddtlInf:
  - *ATR053/* replaces *ATR7*
  - *ATR057/* replaces *ATR6*
  - *FRAD/* replaces *FRAD*
  - *ATR072/* replaces *AT51*
  - *ATR078/* replaces *AT57*
- Additional Information will be used.

The action instructions listed below are not verified by the RTGS platform.

Interbank return request rejection: the first occurrence must start with the value "ATR053/", followed by the reference of the return request of the originator bank.

Further occurrences of the element may be supplied additionally as follows:

- If the LEGL value was used in the “Reason” sub-element “Code”, two further repetitions may optionally be provided to specify the reason for rejection. These must each start with the value "ATR057/". Data protection requirements must be observed if the information is published.
- If the reason given in the "camt.056" of the return request is the value FRAD (Fraudulent origin), another ten repetitions of the element may optionally be supplied. These must each start with the value "FRAD/". By rejecting the request due to "Fraudulent origin", further information may be provided in this element which might permit the money to be legally reclaimed outside of this process. Data protection requirements must be observed if the information is published.

Originator return request rejection: the first occurrence for "Cancellation Status Reason Information" sub-element "Additional Information" must be used starting with the value "ATR072/", followed by the reference of the return request of the originator bank. If the reason given in the "camt.056" of the return request is the value AC03 (Wrong IBAN), another ten repetitions of the element may optionally be supplied. These must each start with the value "ATR078/". By rejecting the request due to "Wrong IBAN", further information may be provided in this element which might permit the money to be legally reclaimed outside of this process. Data protection requirements must be observed if the information is published.

For incoming camt.029 received with additional info with the replacement codes will be stored in EBQA and mapped as per the mapping sheet.

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

## Amount Split for Transfer above EUR 50 Million

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

## SIC and EuroSIC RTGS 2024 Rulebook changes and V3 Clearing directory upload and reachability

SIC and EuroSIC RTGS is an existing clearing supported in Local Clearing vertical under License PPCH24/PPSICH. This document is to cover SIC and EuroSIC RTGS RB 2024 changes for pacs.008, pacs.009, camt.056, camt.029(SEPA),camt.029(Return request rejection), pacs.004, pacs.028 and V3 clearing directory upload and reachability criteria .

As part of rulebook changes 2024 published by SIX, there is a change to the existing tags and flows across pacs & camt messages and the same has been enhanced and updated.

1. The existing version of the message identifiers is changed to newer version, therefore even the xsd should be replaced with the newer version in order to support the latest changes.

   | Message older Version | Message newer Version |
   | --- | --- |
   | camt.029.001.09.ch.02.xsd | camt.029.001.09.ch.03.xsd |
   | camt.056.001.08.ch.03.xsd | camt.056.001.08.ch.04.xsd |  |
2. Transactions greater CHF 100 million and EURI 50 million will be split into multiple messages with unique UETR for each message and will also carry new service level code SPLI.
3. LEI for SEPA payments will not be a sole identifier hence forth.
4. When SEPFCP is initiated/processed Debtor agent and Creditor agents BIC will be supplied under both Name and Any BIC tags of Debtor and Creditor roles respectively.
5. Sub element "Name" for Ultimate Debtor has been enabled for the user to key in.
6. When CSTRTN is initiated at the request of original creditor CUST code will be added in the Return reason code and will be sent out in outgoing pacs.004
7. Also in case of a positive response to the camt.056( FOCR) the additional information field will contain the cancellation id of the received return request.
8. User can now initiate a camt.056 for an outward pacs.009 and pacs.028 of camt.056 with the underlying payment as pacs.009 will be supported.
9. The Initiated pacs.028 to hold the underlying pacs.009 details
10. When a return request/status request is raised for a split payment the corresponding UETR of the underlying payment will sent in Original UETR code along with the service level code.
11. While sending positive response for incoming camt.087 code VADA will be sent out.

### Clearing Directory

As part of latest version 3.0 published by SIC, there is a change to the Clearing Directory file sent by SIC

1. While uploading system to differentiate the version 2.1 and version 3.0 and trigger the respective mapping accordingly.
2. New Mapping for CSV to CA.CLEARING DIRECTORY has been developed.
3. Record should be released in TPS INTERNAL CONFIG for handling of the new CA version change.
4. All values in the clearing directory file should be uploaded to the CA. CLEARING.DIRECTORY in TPH.
5. Context Name and Context Value are used as per the below mapping sheet.

| Clearing Directory Application | T24 upload Record from SIC file |
| --- | --- |
| NCC/BIC | SIC IID |
| Institution Name | Name of Bank |
| City | Town Name |
| Payment Channel | SIC |
| Clearing Parameter |  |
| Scheme | \* |
| Status | ENABLED |
| Reachability Type | D |
| Country | Country |
| Start Date |  |
| End Date |  |
| Upload Date | Today |
| Effective Date | Valid Date |
| Upload File Name |  |
| Purge Eligibility | Yes |
| Context Name.1 | IID |
| Context Value.1 | 3 to 5 digit |
| Context Name.2 | New IID |
| Context Value.2 | 3 to 5 digit |
| Context Name.3 | Concatenation |
| Context Value.3 | Y or N |
| Context Name.4 | IID Type |
| Context Value.4 | Numeric |
| Context Name.5 | QR IID Allocation |
| Context Value.5 | 5 digit Numeric |
| Context Name.6 | SIC |
| Context Value.6 | Y or N |
| Context Name.7 | SICRTGS |
| Context Value.7 | Y or N |
| Context Name.8 | SICIP |
| Context Value.8 | Y or N |
| Context Name.9 | EUSIC |
| Context Value.9 | Y or N |
| Context Name.10 | LSVCHF |
| Context Value.10 | Y or N |
| Context Name.11 | LSVEUR |
| Context Value.11 | Y or N |
| Context Name.12 | Street Name |
| Context Value.12 | Alpha Numeric |
| Context Name.13 | Building Number |
| Context Value.13 | Numeric |
| Context Name.14 | Post Code |
| Context Value.14 | Alpha Numeric |
| Context Name.15 | Headquarters |
| Context Value.15 | Numeric |

### SIC Reachability check based on latest V3 file

- TPH to perform reachability check with the clearing directory to check if the beneficiary bank is a participant in SIC/EuroSIC.
- Reachability should be based on NCC/BIC.
- The below reachability changes should be enabled if the below TPS.INTERNAL.COFIGS record is in place.
- New reachability API is developed to support the below logic.
- If the payment is SIC, then reachability should be checked under the context name: SIC with value as Y or N ( Y – participant, N – Not a participant). Within SIC payment if its RTGS, check for context name SICRTGS value and if its Instant payment, check for context name SICIP and its value.
- If the payment is EUSIC, then reachability should be checked under the context name : EUSIC with value as Y or N ( Y – participant, N – Not a participant).
- If the payment is LSV CHF, then reachability should be checked under the context name : LSVCHF with value as Y or N (( Y – participant, N – Not a participant).
- If the payment is LSV EUR, then reachability should be checked under the context name : LSVEUR with value as Y or N (( Y – participant, N – Not a participant).
- If pain.001 or D10 is received with IID value, the IID value needs to be checked in context Name and if concatenation is N, then the corresponding SIC ID to be replaced in the outgoing message in Creditor Agent and Instructed Agent. The reachability check needs to be checked for the SIC ID under context value of LSV CHF for CHF payment and LSV EUR for EUR payment.
- If pain.001 or D10 is received with IID value, the IID value needs to be checked in context Name and if concatenation is Y, then check for NewIID record. Based on the New IID , corresponding SIC ID to be replaced in the outgoing message in Creditor Agent and Instructed Agent. The reachability check needs to be checked for the SIC ID under context value of LSV CHF for CHF payment and LSV EUR for EUR payment.
- For QR payments, existing reachability is based on NCC or BIC. As part of current V3, the reachability should be done as per below logic.
  - CHF CCY - If its QR payment, System to check the IID-TYPE as 4 and the SIC participant as Y , SIC RTGS participant as Y for CHF. If result is positive, process the payment, if not positive, move the payment to repair queue display the failure error.
  - EUR CCY -If its QR payment, System to check IID-TYPE as 4, and the SIC participant as Y and EUSIC RTGS Participant as Y . If result is positive, process the payment, if not positive, move the payment to repair queue and display the failure error.
- If the reachability fails, payment should be pushed to repair queue stating payment BIC is not reachable.

For V2 file upload please refer column “ SIC/EUROSIC Directory Upload”.

## SIC and EUROSIC Rule Book Changes 2025

### Hybrid Postal Address for all Agents and Parties

**Applicability** – Bank Credit Transfer and Customer Credit Transfer

**Message Types Affected** – All messages for SIC and EuroSIC

From November 2025, the following changes are applicable regarding postal address:

| Address type | Address Rule |
| --- | --- |
| Structured postal address | Postal address must include the Town Name and Country elements as a minimum. It cannot contain the Address Line element. |
| Unstructured postal address | Postal address uses only the Address Line element. 2 occurrences of the Address Line element with up to 70 characters each are permitted. |
| Hybrid (semi-structured) address | A postal address must include the Town Name and Country elements, and it also allows the Address Line element to be included. 2 occurrences of the Address Line element with up to 70 characters each are permitted. Other structured elements in addition to Town Name and Country may also be included e.g. Post Code.  It is recommended (no Validation performed by RTGS) that data present in structured elements within the Postal Address must not, under any circumstances be repeated in Address Line. |

Note the below timeline, which outlines the possible Postal Address options for all Agents and Parties as of Rulebook 2025:

- From November 2025 to November 2026, SIX permits a hybrid (semi-structured), fully structured or fully unstructured postal address.
- From November 2026 onwards, SIX permits a semi-structured (hybrid) or fully structured postal address. Fully unstructured postal addresses are no longer permitted.

The usage of the unstructured Address Line as a standalone element within Postal Address are not supported after November 2026.

[Beneficiary Application](#)

This table illustrates the address details that are captured in Beneficiary application and their mapping to Payment Order Product (POA) or TPH ISO Order Entry screen during payment initiation and the enhancement to the system from November 2025.

| Agents /Parties | System Impact (Yes/no) | Beneficiary Application | Payment Initiation via POA | Payment Initiation Via TPH |
| --- | --- | --- | --- | --- |
| Creditor | Yes | User can currently enter only structured address  System to be enhanced to allow user to enter unstructured address lines  System to be enhanced to raise warning if town name or country is not entered. | Structured address from Beneficiary application is copied to Payment order.  System is enhanced to copy unstructured address from Beneficiary application | Structured address from Beneficiary application is copied to TPH OE Screen.  System is enhanced to copy unstructured address from Beneficiary application  TPH currently performs validation that if structured address is present then town name and country is mandatory. This validation is also now applicable when hybrid address is entered.  If structured address (minimum town and country) and unstructured address details are present for the creditor in the payment instruction, hybrid address is now populated in the outgoing pacs.008 message to SIX |
| Intermediary Agent 1  Intermediary Agent 2  Intermediary Agent 3 | Yes (POA) | User can currently enter only structured (partial fields) or just unstructured or both. There is no validation in the application,    System to be enhanced to raise warning if town name or country is not entered. | Structured address from Beneficiary application is copied to Payment order.  Unstructured address for Intermediary Agent 1 & 2 from Beneficiary application is copied to Payment order product.  System is enhanced to copy unstructured address for Intermediary Agent 1 from Beneficiary application | Not applicable. Details are not copied to TPH OE screen. |
| Creditor Agent | Yes (POA\_ | User can currently enter only structured. There is currently no validation in the application.  System to be enhanced to allow user to enter unstructured address lines.  System to be enhanced to raise warning if town name or country is not entered. | Structured address from Beneficiary application is copied to Payment order.  System is enhanced to copy unstructured address from Beneficiary application | Only Creditor Agent BIC is copied from Beneficiary application to TPH. Address details are not copied, hence no impact |
| Ultimate Creditor | Yes (POA) | User can currently enter only structured or just unstructured or both. There is no validation in the application.  System to be enhanced to raise warning if town name or country is not entered. | Structured address from Beneficiary application is copied to Payment order.  System is enhanced to copy unstructured address from Beneficiary application | Details from Beneficiary application is mapped to TPH OE initiation screen.  TPH currently performs validation that if structured address is present then town name and country is mandatory. This validation is also now applicable when hybrid address is entered.  If structured address (minimum town and country) and unstructured address details are present for the ultimate creditor in the payment instruction, hybrid address is now populated in the outgoing pacs.008 message to SIX. |
| Ultimate Debtor | Yes (POA) | User can currently enter only structured or just unstructured or both. There is no validation in the application.    System to be enhanced to raise warning if town name or country is not entered. | Structured address from Beneficiary application is copied to Payment order product  System is enhanced to copy unstructured address from Beneficiary application | Not applicable. Details are not copied to TPH OE screen. |

[Payment Order Application](#)

This table illustrates the behaviour of the address lines fields in POA for a SIX product (customer transfer and bank transfer) from November 2025

| Agents /Parties | System Impact   (Yes/no) | Description |
| --- | --- | --- |
| Debtor | Yes | When Debtor details are imposed by the user, following validations are performed (warning is raised):   - If only structured address is entered, then town name and country is mandatory - If structured and unstructured is entered, then then town name and country is mandatory   There is currently no validation on the length and number of lines for unstructured address lines entered by the user which continue to be applicable when hybrid address is entered.  When debtor details are not imposed by the user, structured present in T24 customer application is retrieved and stored as part of the payment order. System is enhanced to retrieve unstructured address as well from the customer application |
| Creditor  Intermediary Agent 1  Intermediary Agent 2  Intermediary Agent 3  Creditor Agent | Yes | If only structured address is entered, then town name and country is mandatory (warning is raised).  If structured and unstructured is entered, then then town name and country is mandatory (warning is raised).  There is currently no validation on the length and number of lines for unstructured address lines entered by the user which continue to be applicable when hybrid address is entered. |
| Ultimate Creditor | Yes | If only structured address is entered, then town name and country is mandatory (warning is raised).  If structured and unstructured is entered, then then town name and country is mandatory (warning is raised).  Only unstructured address is not allowed.  There is currently no validation on the length and number of lines for unstructured address lines entered by the user which continue to be applicable when hybrid address is entered. |
| Ultimate Debtor |
| Invoicer  Invoicee  Garnishee  Garnishment Administrator | No | These fields are not present in the payment order application Hence no impact. |

[Sender FI](#)

Sender FIs when acting as the direct participant for a payment originated by DP’s customer (outgoing)

[Message Type: Pacs.008, Pacs.009](#)

| Agents /Parties | System Impact   (Yes/No) | Description |
| --- | --- | --- |
| Debtor | Yes | ISO Order Entry Screen (Customer transfer): When the debtor details are imposed by the user, the user can enter structured address and unstructured address, fully unstructured address in addition to fully structured address (existing feature). In case only structured address is entered, town name and country are mandatory (existing feature). In case of hybrid address, town name and country is made mandatory (New)  When the debit customer is validated with the Account & customer database, unstructured address stored in the customer database is stored in the system. These details are made viewable in the order entry/repair/view screens of the payment transaction.  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the debtor (imposed and not imposed by user), hybrid address is populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.  Above details apply for embedded and standalone (TPH). For Standalone, customer database can be in different instance of T24, Microservice or external Core. |
| Creditor | Yes | ISO Order Entry Screen (Customer transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address. In case only structured address is entered, town name and country are mandatory (existing feature). In case of hybrid address, town name and country is still made mandatory (New).  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the creditor, hybrid address is now populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements. |
| Debtor Agent  Creditor Agent | Yes | ISO Order Entry Screen (Customer transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address.  If structured address (minimum town and country) and unstructured address details are present for the debtor agent, hybrid address is now populated in the outgoing pacs.008 message to SIX.  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70)  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised). |
| Instructing Reimbursement Agent  Instructed Reimbursement Agent    Third Reimbursement Agent | Yes | In ISO order entry screen, user is currently allowed to enter either fully structured address or fully unstructured lines. From November 2025, user can enter structured address (minimum town name and country) along with unstructured address in addition to either fully structured address or fully unstructured address.  If structured address (minimum town and country) and unstructured address details are present for the debtor agent, hybrid address is now populated in the outgoing pacs.008 message to SIX  System currently performs the validation that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  These fields are not applicable for pacs.009 |
| Charge Information/Agent | No | For payments originated by TPH, system does not populate address details for the Charge Information Agent element. So |
| Previous Instructing Agent 1  Previous Instructing Agent 2  Previous Instructing Agent 3 | No | NA.  These agents are not populated in an outgoing pacs.008 originated from TPH bank |
| Intermediary Agent 1    Intermediary Agent 2    Intermediary Agent 3 | Yes | ISO Order Entry Screen (Customer transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address.  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the Intermediary Agent 1 in the payment instruction, hybrid address is now populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements. |
| Ultimate Debtor  Ultimate Creditor | Yes | ISO Order Entry Screen (Customer transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address.  System is enhanced that if only structured address is present then town name and country is mandatory for order entry and repair payments (warning raised).  Also, enhancement would be done to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the ultimate debtor in the payment instruction, hybrid address is now populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.  For ultimate debtor, there can be either structured address or hybrid address. Fully Unstructured address is not allowed. |
| Initiating Party |  | ISO Order Entry Screen (Customer transfer): There is no field for the user to enter initiating party.  If structured address (minimum town and country) and unstructured address details are present for the Initiating Party in the payment instruction, hybrid address is now populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.  Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised)  There can be either structured address or hybrid address. Fully Unstructured address is not allowed |
| Invoicer    Invoicee    Garnishee    Garnishment Administrator |  | ISO Order Entry Screen (Customer transfer): There is no field for the user to enter these parties  When the details are received from client channels via pain.001, the details are stored as a BLOB in the system.  System does not perform any validation. Assumption is that the address details are either structured or hybrid. System maps the details stored in the BLOB in the outgoing message.  There can be either structured address or hybrid address. Fully Unstructured address is not allowed |

[Message Type: pacs.009COV](#)

| Agents /Parties | System Impact | Description |
| --- | --- | --- |
| Debtor Agent | No | If debtor Agent is populated, then it is only the TPH Company BIC that is sent out (no impact ). |
| Creditor Agent    Intermediary Agent 1  Creditor | Yes | In ISO order entry screen, user is currently allowed to enter either fully structured address or fully unstructured lines. From November 2025, user can enter structured address (minimum town name and country) along with unstructured address in addition to either fully structured address or fully unstructured address.  System currently performs the validation that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  Above validation is applicable for payment instruction received from client channels and for which cover is generated by the payment system  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70). |
| Previous Instructing Agent 1  Previous Instructing Agent 2  Previous Instructing Agent 3 | No | Not applicable |
| Debtor | No | TPH company BIC is populated without address details, hence no impact. |

[Message Type: pacs.004](#)

| Agents /Parties | System Impact | Description |
| --- | --- | --- |
| Debtor Agent  Creditor Agent  Intermediary Agent 1  Intermediary Agent 2  Intermediary Agent 3  Previous Instructing Agent 1  Previous Instructing Agent 2  Previous Instructing Agent 3 | Yes | ISO Order Entry Return Screen (Customer transfer & Bank Transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address.  For returns generated by the system, the details from the original payment are copied to the return payment (reverse role mapping)  If structured address (minimum town and country) and unstructured address details are present for the debtor agent, hybrid address is now populated in the outgoing pacs.008 message to SIX.  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70)  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  There no fields present in the ISO Order entry Return screens for Previous Instructing Agent1 ,2 & 3. |
| Charge Information/Agent | No | There is no field in the Order Entry Return screen  For the fees calculated by TPH, TPH Company BIC is populated in the outgoing pacs.004. |
| Creditor | Yes | ISO Order Entry Return Screen (Customer transfer & Bank Transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address. In case only structured address is entered, town name and country are mandatory (existing feature). In case of hybrid address, town name and country are made mandatory (New).  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the creditor, hybrid address is now populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements. |
| Debtor | Yes | ISO Order Entry Return Screen (Customer transfer): When the debtor details are imposed by the user, the user can enter structured address and unstructured address, fully unstructured address in addition to fully structured address (existing feature). In case only structured address is entered, town name and country are mandatory (existing feature). In case of hybrid address, town name and country are made mandatory (New)  When the debit customer is validated with the Account & customer database, unstructured address stored in the customer database is stored in the system to accommodate 2 lines of max 70. These details are made viewable in the order entry/repair/view screens of the payment transaction.  System does not currently validate for existence of only structured address or unstructured when address is present. This is the case even after November 2025. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised). System is enhanced to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the debtor (imposed and not imposed by user), hybrid address is populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.  Above details apply for embedded and standalone (TPH). For Standalone, customer database can be in different instance of T24, Microservice or external Core. |
| Ultimate Debtor  Ultimate Creditor | Yes | ISO Order Entry Returns Screen (Customer transfer): User is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address.  For returns generated by the system, the detail from the original payment is copied to the return payment (reverse role mappings)  System is enhanced that if only structured address is present then town name and country is mandatory for order entry and repair payments (warning raised).  Also, enhancement would be done to validate that when hybrid address is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the ultimate debtor in the payment instruction, hybrid address is now populated in the outgoing pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.  There can be either structured address or hybrid address. Fully Unstructured address is not allowed. |
| Initiating Party | No | TPH does not populate initiating party for an outgoing return |
| Invoicer  Invoicee  Garnishee  Garnishment Administrator | Yes | There are no fields in the Order entry Return screen for these fields.  The details for these parties received in the incoming message are stored in a BLOB. They are sent in the outgoing message as received in the blob.  If structured address (minimum town and country) and unstructured address details are present in the payment instruction, hybrid address is now populated in the outgoing pacs.004 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70). |
| Originator | Yes | If the return is originated by the TPH bank, only BIC is populated. Hence no impact  If the return is originated by the customer, then address details received for the original beneficiary are populated in the originator tag element.  If structured address (minimum town and country) and unstructured address details are present in the payment instruction, hybrid address is now populated in the outgoing pacs.004 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70). |

Sender FIs when acting as the intermediary participant for a payment sent to RTGS SIX (Redirected)

| Agents /Parties | Message Types | System Impact | Description |
| --- | --- | --- | --- |
| Debtor Agent | Pacs.008, pacs.009, pacs.009COV, pacs.004 | Yes | System currently validates for existence of town name or country when only structured address is present.  System does not validate for existence of town name or country when structured and unstructured is entered.  If structured address (minimum town and country) and unstructured address details are present for the debtor (imposed and not imposed by user), hybrid address is populated in the redirected pacs.008 message to SIX.  When hybrid address is populated, system must ensure that only max 2 occurrences of address lines is present (each having a max length of 70).  If there are more than 140 characters of unstructured address line details in addition to structured address (with town name and country) then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements. |
| Creditor Agent | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Instructing Reimbursement Agent | Pacs.008 |
| Instructed Reimbursement Agent | Pacs.008 |
| Third Reimbursement Agent Charge Information | Pacs.008 |
| Charge Information/Agent | Pacs.008, pacs.004 |
| Previous Instructing Agent 1 | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Previous Instructing Agent 2 | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Previous Instructing Agent 3 | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Intermediary Agent 1 | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Intermediary Agent 2 | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Intermediary Agent 3 | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Creditor | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Debtor | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Ultimate Debtor | Pacs.008, pacs.009COV, pacs.004 |
| Ultimate Creditor | Pacs.008, pacs.009COV, pacs.004 |
| Initiating Party | Pacs.008, pacs.009COV, pacs.004 |
| Originator | Pacs.004 |
| Invoicer | Pacs.008, pacs.009COV, pacs.004 | No | Details received for these parties are stored as a BLOB. If hybrid address is received, it automatically becomes part of the BLOB and sent as part of the redirected message. Hence no impact |
| Invoicee | Pacs.008, pacs.009COV, pacs.004 |
| Garnishee | Pacs.008, pacs.009COV, pacs.004 |
| Garnishment Administrator | Pacs.008, pacs.009COV, pacs.004 |

[Message Type: camt.056, camt.029](#)

| Agents /Parties | System Impact   (Yes/No) | Description |
| --- | --- | --- |
| Creator | Yes | - Outward – Recalls - System sends hybrid or structured or unstructured depending on what is available in the underlying payment. - Outward – ROI - System sends hybrid or structured or unstructured depending on what is available in the recall received   - Above details apply for embedded and standalone (TPH). For Standalone, customer database can be in different instance of T24, Microservice or external Core. - There can be either structured address or hybrid address. Fully Unstructured address is not allowed |
| Originator | Yes | Outward – Recalls - System sends hybrid or structured or unstructured depending on what is available in the underlying payment.  Outward – ROI - System sends hybrid or structured or unstructured depending on what is available in the recall received  Above details apply for embedded and standalone (TPH). For Standalone, customer database can be in different instance of T24, Microservice or external Core.  Note: There can be either structured address or hybrid address. Fully Unstructured address is not allowed |

[Receiver FI](#)

This table describes the impact where the TPH is acting as a receiving FI and the customer is 'On Us’. Direction of the payment is 'Incoming'.

| Agents /Parties | Message Types | System Impact  (Yes/No) | Gap Details |
| --- | --- | --- | --- |
| Debtor Agent \* | Pacs.008, pacs.009, pacs.009COV, pacs.004 | No | In the Order Entry Screen, user is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address. There is no validation as these messages are received from the clearing and keyed in manually  Address details (structured & unstructured) received in the payment instruction are currently stored in the system and accordingly displayed on the screen. This continues for hybrid address as well and there is no impact. |
| Creditor Agent \* | Pacs.008, pacs.009, pacs.009COV, pacs.004 |
| Instructing Reimbursement Agent \* | Pacs.008 | No | These fields are not present in OE incoming screen  Address details (structured & unstructured) received in the payment instruction are currently stored in the system and accordingly displayed on the screen. This continues for hybrid address as well and there is no impact. |
| Instructed Reimbursement Agent \* | Pacs.008 |
| Third Reimbursement Agent Charge Information \* | Pacs.008 |
| Charge Information/Agent | Pacs.008, pacs.004 | No | Charge Agent details are not present in OE incoming CTR screen  Address details (structured & unstructured) received in the payment instruction are currently stored in the system but NOT displayed on the screen. This continues for hybrid address as well and there is no impact. |
| Previous Instructing Agent 1 | Pacs.008, pacs.009, pacs.009COV, pacs.004 | No | In the Order Entry Screen, user is currently allowed to enter structured address and unstructured lines in addition to either fully structured address or fully unstructured address. There is no validation as these messages are received from the clearing and keyed in manually  Address details (structured & unstructured) received in the payment instruction are currently stored in the system and accordingly displayed on the screen. This continues for hybrid address as well and there is no impact. |
| Previous Instructing Agent 2 |
| Previous Instructing Agent 3 |
| Creditor |
| Debtor |
| Ultimate Debtor | Pacs.008, pacs.009COV, pacs.004 |
| Ultimate Creditor |
| Intermediary Agent 1 | Pacs.008, pacs.009, pacs.009COV, pacs.004 | NA | For an 'On us’ payments, there are no intermediary agents. |
| Intermediary Agent 2 |
| Intermediary Agent 3 |
| Initiating Party | Pacs.008, pacs.009COV, pacs.004 | No | Field is not present in OE incoming screen.  Address details (structured & unstructured) received in the payment instruction are currently stored in the system but NOT displayed on the screen. This continues for hybrid address as well and there is no impact. |
| Invoicer | Pacs.008, pacs.009COV, pacs.004 | No | These fields are not present in OE incoming screen.  When payment instruction is received from the clearing, these parties are stored as a BLOB. If hybrid address is received, it automatically becomes part of the BLOB and hence no impact. They are not displayed on the view screen |
| Invoicee |
| Garnishee |
| Garnishment Administrator |
| Originator | pacs.004, pacs.002 | No | - pacs.004: Address details (structured & unstructured) received in the payment instruction are currently stored in the system but NOT displayed on the screen. This continues for hybrid address as well and there is no impact. - pacs.002: Address details are not stored in the system and hence no impact. |
| Creator | Camt.056, camt.029 | No | Address details (structured & unstructured) received in the recall and resolution of investigation messages are currently stored in the system and displayed on the screen. This continues for hybrid address as well and there is no impact. |
| Originator | Camt.056, camt.029 | No | Address details (structured & unstructured) received in the recall and resolution of investigation messages are currently stored in the system and displayed on the screen. This continues for hybrid address as well and there is no impact. |

For Agents, only few details of the structured address details (Town name, Post code, Country) are currently displayed on the screens.

There is no Order Entry Incoming screen for pacs.004 and pacs.008.

### Debtor and Creditor to support Hybrid Postal Address – EuroSIC SEPA

A new type of address called 'Hybrid’ address has been introduced in SEPA 2025 specification. This is in addition to the structured and unstructured address that SEPA currently supports. Definition of the address types are as below.

- **Structured Address** - Town Name and Country are mandatory among all other structured address fields\*. Address lines are not allowed.
- **Unstructured Address** - Address lines and country are allowed. At least one occurrence of address line is mandatory. Other structured address fields are not allowed. Use of 'Country’ is mandatory when either the Debtor Agent or Creditor Agent is located in a non-EEA SEPA country or territory. (euroSIC RTGS does not check)
- **Hybrid Address** - All structured fields along with address lines are allowed. Town Name, Country and at least one occurrence of Address line (max 2 lines with 70 characters each) are mandatory. (newly added in SEPA 2025)

Hybrid address is supported. Unstructured address is not supported by SEPA (via EPC mandate) post Nov 2026. Banks have one year (Nov 2025 to Nov 2026) to transition from unstructured address to Structured address or Hybrid address. Only one among the above three address type is accepted.

Structured address fields are Department, Sub-Department, Street Name, Building Number, Building Name, Floor, Post Box, Room, Postal Code, Town Name, Town Location Name, District Name, Country Sub-Division, and Country.

Temenos Payments already supports Structured Address and Unstructured Address. It started supporting Hybrid Address with SEPA EPC 2025 updates.

The affected message types are pacs.008, pacs.004, camt.056, camt.027 and camt.087, and pacs.028.

[Payment Order Application](#)

This table illustrates the behaviour of the address lines fields in POA for a EuroSIC product (Payment Type as SEPPMT or SEPFCP) from October 2025.

| Agents  /Parties | System Impact  (Yes/no) | Description |
| --- | --- | --- |
| Debtor | Yes | When Debtor details are imposed by the user, following validations are performed (warning is raised):   - If only structured address is entered, then town name and country is mandatory (existing) - If structured (other than country) and unstructured is entered, then town name and country is mandatory (change)   There is currently no validation on the length and number of lines for unstructured address lines entered by the user which continue to be applicable when hybrid address is entered.  When debtor details are not imposed by the user, structured present in T24 customer application is retrieved and stored as part of the payment order. System has been enhanced to retrieve unstructured address as well from the customer application. |
| Creditor | Yes | If only structured address is entered, then town name and country is mandatory (Existing).  If structured (other than country) and unstructured is entered, then town name and country is mandatory (warning is raised).  There is currently no validation on the length and number of lines for unstructured address lines entered by the user which continue to be applicable when hybrid address is entered. |

[Originating PSP](#)

New parameter in TPH Clearing Module to enable hybrid address (*Address Type* field in CLEARING) for a given clearing. This parameter must be enabled for SIC/ESIC Clearing (PPSICH) when hybrid address change goes-live.

- For Debtor: At least one occurrence of 'Address line’ is mandatory. 'Postal Address’ sub-elements other than 'Address Line’ and 'Country’ are forbidden. The use of 'Country’ is mandatory when either the Debtor Agent or Creditor Agent is located in a non-EEA SEPA country or territory
- Solution: Clearing specific validation ensures this is checked for payment type SEPPMT, SEPFCP

[Message Type: Pacs.008 & pacs.004](#)

| Agents /Parties | System Impact  (Yes/No) | Description |
| --- | --- | --- |
| Debtor | Yes | When the debit customer is validated with the Account & customer database, unstructured address stored in the customer database is stored in the system. These details are made viewable in the view screens of the payment transaction.  System does not currently validate for existence of only structured address or unstructured when address is present. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised).  System is enhanced to validate that when structured (other than country) and unstructured is present then town name and country is mandatory (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the debtor, hybrid address is populated in the outgoing pacs.008 /pacs.004 message to EuroSIC SEPA.  If unstructured address and only country is present for structured address, then unstructured address along with country is sent in the outgoing message  For hybrid address, if there are more than 140 characters of unstructured address lines then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.  Note: Above details apply for embedded and standalone (TPH). For Standalone, customer database can be in different instance of T24, Microservice or external Core. |
| Creditor | Yes | System does not currently validate for existence of only structured address or unstructured when address is present. Only validation that is currently performed is that if only structured address is present then town name and country is mandatory (error raised).  System is enhanced to validate that when structured (other than country) and unstructured is present then town name and country is mandatory for order entry and repair payments (warning is raised).  If structured address (minimum town and country) and unstructured address details are present for the creditor, hybrid address is populated in the outgoing pacs.008/pacs.004 message to EuroSIC SEPA.  If there are more than 140 characters of unstructured address lines, then only 140 characters would be sent out with 70 characters in each in the 2 address lines tag elements.    Note: Above details apply for embedded and standalone (TPH). For Standalone, customer database can be in different instance of T24, Microservice or external Core. |

[Receiver PSP](#)

No change as all the fields in postal address are stored in respective fields in POR tables for Debtor and Creditor.

In this topic

- [Introduction to Swiss Interbank Clearing (SIC)](#IntroductiontoSwissInterbankClearingSIC)

- [Amount Split for Transfer above CHF 100 Million](#AmountSplitforTransferaboveCHF100Million)
- [Receive camt.025 with ACCP or RJCT Status](#Receivecamt025withACCPorRJCTStatus)
- [Category Purpose](#CategoryPurpose)
- [Instruction for Next Agent](#InstructionforNextAgent)
- [Remittance Information](#RemittanceInformation)
- [Service Level](#ServiceLevel)
- [Time Indication](#TimeIndication)
- [Message Priority](#MessagePriority)
- [Regulatory Reporting](#RegulatoryReporting)
- [Inward camt.025 Processing for Outward Messages](#Inwardcamt025ProcessingforOutwardMessages)
- [QR Billing for SIC and euroSIC Clearing](#QRBillingforSICandeuroSICClearing)
- [LSV Direct Debit](#LSVDirectDebit)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)
- [SIC and EuroSIC Rulebook for Bank Credit Transfer for pacs.009](#SICandEuroSICRulebookforBankCreditTransferforpacs009)
- [SIC and EuroSIC Rulebook for camt.025, camt.029 and camt.056](#SICandEuroSICRulebookforcamt025camt029andcamt056)
- [SIC and EuroSIC Rulebook for camt.029 (SEPA) and pacs.028](#SICandEuroSICRulebookforcamt029SEPAandpacs028)
- [Amount Split for Transfer above EUR 50 Million](#AmountSplitforTransferaboveEUR50Million)
- [SIC and EuroSIC RTGS 2024 Rulebook changes and V3 Clearing directory upload and reachability](#SICandEuroSICRTGS2024RulebookchangesandV3Clearingdirectoryuploadandreachability)
- [SIC and EUROSIC Rule Book Changes 2025](#SICandEUROSICRuleBookChanges2025)

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
Tuesday, April 14, 2026 4:19:07 PM IST