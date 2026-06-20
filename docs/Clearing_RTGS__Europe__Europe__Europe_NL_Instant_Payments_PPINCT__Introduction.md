# Introduction to Netherlands (NL) Instant Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
    - [Introduction](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
    - [Configuration](../../Europe/Europe_NL_Instant_Payments_PPINCT/Configuration.htm)
    - [Working with](../../Europe/Europe_NL_Instant_Payments_PPINCT/Working_with.htm)
    - [Tasks](../../Europe/Europe_NL_Instant_Payments_PPINCT/Tasks.htm)
    - [Outputs](../../Europe/Europe_NL_Instant_Payments_PPINCT/Outputs.htm)
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

# Introduction to Netherlands (NL) Instant Payments

Updated On 10 July 2025 |
 17 Min(s) read

Feedback
Summarize

Temenos Payment Hub (TPH) can process payments sent or received from the NL Instant Clearing by using the existing Instant Clearing Framework. EquensWorldline Clearing and Settlement Mechanism is the CSM for clearing Instant Payments in Netherlands and is based on SEPA scheme. This allows a maximum transaction limit of EUR 100000 for EQUENS instant payments.

TPH supports the EPC SEPA 2020 rulebook changes.

The process flow of NL Instant Payments is given below:



1. The originator bank (TPH) receives an Instant Payment instruction from the originator. Additionally, performs the following actions:

- After the receipt of the transaction and user’s authentication, it generates the timestamp.
- Validates the instruction and reserves the amount on the client’s account.
- Creates the SCT instant transaction.

2. The originator bank sends the SCT instant transaction message to the originator CSM.
3. The originator bank CSM forwards the SCT instant transaction message to the beneficiary bank using the beneficiary bank CSM.
4. The beneficiary bank sends the confirmation message to the CSM indicating the following:

- Received the SCT instant transaction
- Process the SCT instant transaction (positive confirmation) instantly

5. CSM performs the following:

- Executes the clearing on the respective accounts
- Debits the originator bank
- Credits the beneficiary bank
- Notifies both the sender and beneficiary of the execution

6. The originator bank debits its client’s account (by the amount reserved in step 1).
7. The beneficiary bank instantly makes the received funds available to the beneficiary after receiving the settlement confirmation from CSM (as a response to the positive confirmation message sent in step 4).

[Types of Payments and Messages](#)

TPH supports the following NL Instant Payment message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.02 | B2B | Customer credit transfer | Inward and outward |
| pacs.004.001.02 | B2B | Return | Inward and outward |
| camt.056.001.01 | B2B | Payment cancellation request or Request for recall | Inward and outward |
| camt.029.001.03 | B2B | Resolution of investigation | Inward and outward |
| pacs.028 | B2B | Payment status request | Inward and outward |
| pacs.002.001.03 | B2B | Clearing payment status report | Inward |
| pain.001.001.03 | C2B | Credit transfer initiation | Inward |
| pain.002.001.03 | B2C | Payment status report to customer | Outward |

[Bank Identifier Code (BIC) and IBAN](#)

The preferred bank or branch and beneficiary account identification methods used in NL Instant Payment are BIC and IBAN, respectively.

[Payment Schemes](#)

TPH supports the following payment schemes for NL Instant payments:

| Payment Schemes | Description |
| --- | --- |
| INST | Instant credit transfer |
| INSTTC01 | Time critical instant credit transfer under the rules of the Dutch AOS on top of the EPC SCT Instant scheme |
| INSTNT01 | Non- time critical instant credit transfer under the rules of the Dutch AOS on top of the EPC SCT Instant scheme |

[Initiating NL Instant Payment](#)

NL credit transfer can be initiated using the following:

|  |  |
| --- | --- |
| pain001 | - NL Instant Payment can be received using pain.001. - System supports both single and bulk pain.001. - Pain.001 can result in book transfers (beneficiary in the books of the processing bank) or an outward transfer (pacs.008 is sent to clearing). |
| Payment Order | - NL Instant can be initiated from the payment order. - User needs to enter the following details:  - Ordering customer - Beneficiary customer - Payment amount - Payment currency - Requested execution date or credit value date (calculated based on PO product configuration)  - Validate the payment order and commit the record. - Authoriser authorises the payment order, and system processes as a book or an outward payment depending on where the beneficiary resides. For outward payments, pacs.008 message is generated and sent to clearing. |

TPH supports the following local instrument codes for NL Instant Payments:

| Local Instrument Codes | Description |
| --- | --- |
| INST | Instant credit transfer |
| INSTTC01 | Instant credit transfer time critical under the rules of the Dutch AOS on top of the EPC SCT Inst scheme |
| INSTNT01 | Instant credit transfer non-time critical under the rules of the Dutch AOS on top of the EPC SCT Inst scheme |

[Rejection from CSM](#)

CSM rejects the payment transaction, when it:

- Fails in the content validation
- Cannot reserve the amount necessary for settlement on the originator bank’s account (lack of funds)

TPH (originator bank) receives a negative final status report from CSM with the appropriate reason code, and without the amount reserved on the account of the originator bank.

[Rejection by the Beneficiary Bank](#)

The beneficiary bank can reject the instant payment transaction due to formatting and/or content problems. For example, if the final beneficiary indicated in the transaction cannot be identified by the bank. A negative status report is sent to CSM as a notification with the relevant reason code for rejection. The process of the Instant Payment transaction ends with the CSM sending final status reports to both the sending and receiving participants about the failure of the transaction while releasing the reservation on the funds.

[Investigation Message](#)

If the originator bank does not receive a confirmation message by the timeout limit, the originator bank sends the investigation message to enquire the status of the original instant payment (pacs.008). The pacs.028 message is sent as investigation message to CSM. The investigation message can be triggered automatically based on the configuration. Clearings allow to send the status investigation messages only after certain period measured from the *AcceptanceDateTime* of the instant message. This period varies between different schemes of instant payments. For example, the following are mandatory for clearing:

- For scheme INST − 20 seconds
- For scheme INSTTC01 − 7 seconds
- For scheme INSTNT01 − 72 hours

To know more, refer to [Configuration](Configuration.htm#top) section.



[Responding to a Recall Request](#)

The system lists all the recall requests received in an enquiry. The user responds to it through an user interface in TPH. To know more, refer to [Working with](Working_with.htm#top) section. After receiving the eW Inst Recall from the originator bank, the beneficiary bank needs to provide the response within 15 business days by using one of the following reason codes:

| Reason Code | Description |
| --- | --- |
| AM04 | Insufficient funds on the account |
| ARDT | Already returned transaction |
| CUST | Customer decision |
| NOAS | No response from beneficiary |
| AC04 | Account closed |
| LEGL | Legal decision |
| NOOR | No original transaction received |

If a response is not received from the beneficiary bank, it sends the following negative (camt.029) reason code to the originator bank (automatically) during Close of Business (COB).

| Reason Code | Description |
| --- | --- |
| NOAS | No response from beneficiary |

[Recalling the Request Generation](#)

A recall request is generated and a positive confirmation is received as a response for the request. It is initiated when originator bank wants to recall a previously settled NL instant transaction.

A recall can be initiated by the originator bank or customer’s request.

| Originator Bank | Customer Request |
| --- | --- |
| Recall is initiated based on the following reasons:  - Duplication sending (error code - DUPL) - Technical problems resulting in erroneous SCT instant (error code - TECH) - Fraudulent originated SCT instant (error code - FRAD)  The beneficiary bank needs to provide an answer for the eW instant recall within 15 banking business days (instead of 10 banking days earlier) following the receipt of the eW instant recall from the originator bank. | Recall is initiated based on the following reasons:  - Wrong amount (error code - AM09) - Wrong IBAN (error code - AC03) - Requested by customer without any specified reason (error code - CUST)  A recall is initiated on the last day of the 13th month after the original transaction. |



[Requesting for Status Update](#)

If the originator bank does not receive a confirmation message for the cancellation request (camt.056) sent to beneficiary bank, it sends the investigation message to enquire the status. The pacs.028 message is sent as investigation message to CSM. The beneficiary bank responds as follows:

- pacs.004 for positive response
- camt.029 for negative response



[Final Acceptance Date Time from EquensWorldLine](#)

If the originator or beneficiary bank receives the positive confirmation message from CSM, then the message (pacs.002) has the final acceptance date in *Account Servicer Reference* field and reconciliation cycle ID in clearing *System Reference* field. TPH uses the retrieved final acceptance date while booking the payment in Nostro account (maintained with the clearing institution), provided it is configured for the following,

After receiving the confirmation from clearing, the accounting entries (booking in the ledger) for the outgoing payment (pacs.008) are raised.

To use the settlement date as value date in the Confirmation (pacs.002), while raising the accounting entries.

[Bulking Criteria](#)

NL INST payments files are sent to CSM as individual payment (that is, one transaction for each file).

[Retrieving Original Credit Transfer](#)

On receiving the incoming camt.056 or camt.029 message, the original credit transfer message is retrieved based on the following matching conditions:

- Transaction amount
- Settlement date
- Original transaction ID in the R-Transaction against transaction ID (original payment)

## Equens Instant 2021 Rule Book Changes

The rulebook change functionality introduces the following changes:

- Process an inward and outward bank cancellation request with reason code as FRAD within 13 months from the execution date of the original instant credit transfer. The cancellation acceptance period for other bank cancellation reason codes (TECH or DUPL) remains unchanged at 10 business days.
- The Additional Information tag of camt.029 instant recall negative response has been updated to mandatory and the multiplicity has been increased to 13.
- A new purpose code (RRTP) has been published in the Equens rule book to link RTPs with instant payments. The *Purpose/Code* field in the instant transaction (pacs.008) is populated with a new ISO Code (RRTP) to indicate that the transaction is for a preceding RTP to help in reconciliation of payments at both the ordering and the beneficiary end.

## Equens Instant Rulebook Changes for 2023

This functionality allows banks to support the Equens CT clearing functionality with the latest up to date rulebook changes published for 2023, respectively enhancing the outward and inward for the below messages.

| Messages | Transaction Type |
| --- | --- |
| pacs.008 | Credit Transfer |
| pacs.002 | Clearing status report |
| camt.056 | Cancellation Request |
| camt.029 | Resolution of Investigation |
| pacs.004 | Return Credit Transfer |
| pacs.028 | Status Request |

The Equens RB change enables the migration to the 2019 version of the ISO 20022 and thus, offers the end user the opportunity of using the features under the 2019 version which may not be available under earlier versions of the ISO 20022 standard.

- The existing version of the message identifiers is changed to a newer version, therefore even the xsd will be replaced with the newer version in order to support the latest changes.

  | Message older version | Message new version |
  | --- | --- |
  | pacs.008.001.02 | pacs.008.001.08 |
  | pacs.002.001.03 | pacs.002.001.10 |
  | camt.056.001.01 | camt.056.001.08 |
  | camt.029.001.03 | camt.029.001.09 |
  | pacs.004.001.02 | pacs.004.001.09 |
  | pacs.028.001.01 | pacs.028.001.03 |
- The reference *Id*'s can now contain internal spaces, however leading/trailing spaces are not allowed.
- The element “BIC” (2009 message version) is changed to “BICFI” (2019 message version) and the element “BICOrBEI” (2009 message version) is changed to “AnyBIC” (2019 message version).
- LEI is a new sub-element introduced under the organisation identification for debtor, creditor, ultimate debtor and ultimate creditor. When the organisation identification is used either AnyBIC, LEI or One occurrence of Other must be present. Its is a 20-digit alphanumeric characters value.
- After the RB change 2023 payment, end-users can benefit from the standard delivery of structured address details about the payer and the payee. It consists of Country and TownName (both mandatory) together with one or more of the other structured elements Department, SubDepartment, StreetName, BuildingNumber, BuildingName, Floor, PostBox, Room, PostCode, TownLocationName, DistrictName and CountrySubDivision. The user has the option to capture either the Structured or Unstructured address. The current unstructured PostalAddress can be used in combination with country.
- Proxy is a new sub element (optional) under the Debtor Account and Creditor Account tag. It is optional, it can be used in addition to the (mandatory) IBAN, it doesn’t replace the IBAN. When used, the proxy identification is mandatory and character limit cannot exceed 320 alphanumeric in length.
- Creditor reference information can be used to capture the remittance information and when used, then the structure type, structure issuer and structure reference are mandatory.
- Original message name identification in the R messages now will contain the complete version of the original underlying message.
- The proprietary reasons codes TECH, FRAD, AC03 and AM09 in camt.056 and the proprietary codes AC04, AM04, NOAS, NOOR and ARDT in camt.029 are now moved under the reason codes and usage of the additional information now will be based on the allowed reason under the ISO reason codes.
- Element Purpose is now present in the R messages and the value must be present if it was present in the original message.
- New sub element party is introduced for all the party role tags - Debtor, Creditor, Ultimate Debtor, Ultimate Creditor. For example: Dbtr\_Nm changed to Dbtr\_Pty\_Nm.
- The element Charges Information sub-element Party is replaced by Agent. As a result, in the pacs.004 Positive Response to Recall ChrgsInf\_Pty\_FinInstnId\_BIC is changed to ChrgsInf\_Agt\_FinInstnId\_BICFI.

## Illustrating Model Parameters

To know more on parameter setup for Netherlands Instant Payments, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

NL Instant module can send and receive NL Instant payments in Netherlands clearing.

## Equens Instant Rule Book Changes Addendum 2023

This functionality supports the latest Equens Rulebook change (Addendum 2023) which got published in January 2024 for Instant payments in Netherlands.

Please find the list of changes that were introduced as part of Equens Addendum 2023 changes:

- WORDLINE will be sending the Directory file to all participant banks with file format as rocs.002.002.03 (existing version rocs.002.002.02)
- Inclusion of new element <MaxAmount> in the directory file

## Equens Instant CT Rulebook Changes for 2025

The rulebook changes 2025, published by Equens Worldline, includes the following changes:

1. 'Acceptance Timestamp' in the clearing message includes an option to include milliseconds details.
2. There is no Maximum Transaction limit for SCT Instant payments.
3. Users can now populate the Organization ID details in all three forms (BIC, LEI , and/or other identification for debtor and ultimate debtor).
4. Debtor and creditor are allowed to use either Fully Structured or Fully Unstructured (three lines of address with a maximum of 35 characters each) or Hybrid Address (with structured address and two address lines with a maximum length of 70 characters each).
5. Originator PSPs are not allowed to send more than one recall and/or RFRO (duplicate request) for the same initial SCT Instant payment.
6. The Reach file format has been changed from rocs.002.002.03 to rocs.002.002.04, and some of the tag element names have been changed.
7. The target maximum execution time for the Originator PSP to receive either the message that the ‘Funds have been Made Available to the Beneficiary by the Beneficiary PSP’ or ‘SCT Inst Transaction has been rejected’ is reduced from the current 10 seconds to 5 seconds.
8. Time-Out Deadline at Beneficiary CSM (for INST scheme) to receive either a positive or a negative confirmation message is reduced from the current 20 seconds to 7 seconds.
9. For Outgoing payments to Equens Clearing, Verification of Payee is enabled during payment initiation from Payment Order version.

In this topic

- [Introduction to Netherlands (NL) Instant Payments](#IntroductiontoNetherlandsNLInstantPayments)

- [Equens Instant 2021 Rule Book Changes](#EquensInstant2021RuleBookChanges)
- [Equens Instant Rulebook Changes for 2023](#EquensInstantRulebookChangesfor2023)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)
- [Equens Instant Rule Book Changes Addendum 2023](#EquensInstantRuleBookChangesAddendum2023)
- [Equens Instant CT Rulebook Changes for 2025](#EquensInstantCTRulebookChangesfor2025)

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
Tuesday, April 14, 2026 4:18:52 PM IST