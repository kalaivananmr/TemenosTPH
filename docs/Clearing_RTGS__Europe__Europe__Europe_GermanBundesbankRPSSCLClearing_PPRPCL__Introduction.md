# Introduction to German Bundesbank RPSSCL Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm) > Introduction

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
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
    - [Introduction](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
    - [Configuration](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Configuration.htm)
    - [Working with](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/WorkingWith.htm)
    - [Tasks](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Tasks.htm)
    - [Outputs](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Outputs.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to German Bundesbank RPSSCL Clearing

Updated On 20 January 2026 |
 10 Min(s) read

Feedback
Summarize

This module supports all the messages and flows as per the EPC SEPA, it manages the SEPA based credit transfers and direct debits scheme operated by the Bundesbank Germany.

## Rulebook Changes for RPSSCL

This functionality allows banks to manage in Temenos Payments Hub any new rulebook regulatory changes published by the clearing.

New configuration records have been released to support the RPS SEPA Clearer (RPSSCL) changes. The `PAYMENT.ORDER,RPSSCL.INPUT` version has been created to allow users to initiate RPSSCL payments.

## RPSSCL CT Rulebook change 2023

The RPSSCL RB change enables migration to the 2019 version of ISO 20022 and offers end user the possibility to use the features under the 2019 version that may not be available under earlier versions of the ISO 20022 standard.

The following are the list of rulebook changes introduced as part of RPSSCL SEPA CT Rulebook 2023.

- The existing version of the message identifiers is changed to newer version, therefore even the xsd should be replaced with the newer version in order to support the latest changes.


  | Message older version | Message new version |
  | --- | --- |
  | pacs.008.001.02 | pacs.008.001.08 |
  | pacs.002.001.03 | pacs.002.001.10 |
  | camt.056.001.01 | camt.056.001.08 |
  | camt.029.001.03 | camt.029.001.09 |
  | pacs.004.001.02 | pacs.004.001.09 |
  | pacs.028.001.01 | pacs.028.001.03 |
- The element “BIC” (2009 message version) changed to “BICFI” (2019 message version) and the element “BICOrBEI” (2009 message version) changed to “AnyBIC” (2019 message version).
- LEI is a new sub-element introduced under the organisation identification for debtor, creditor, ultimate debtor and ultimate creditor. When organisation identification is used either AnyBIC, LEI or One occurrence of Other must be present. Its is a 20-digit alphanumeric characters value.
- After the RB change 2023 payment end-users can benefit from the standard delivery of structured address details about the payer and the payee. It consists of Country and TownName(both mandatory) together with one or more of the other structured elements Department, SubDepartment, StreetName, BuildingNumber, BuildingName, Floor, PostBox, Room, PostCode, TownLocationName, DistrictName and CountrySubDivision. The user has the option to capture either Structured or Unstructured address. The current unstructured PostalAddress can be used in combination with country
- Proxy is a new sub element (optional) under the Debtor Account and Creditor Account tag. It is optional, it can be used in addition to the (mandatory) IBAN, it doesn’t replace the IBAN. When used proxy identification is mandatory and character limit cannot exceed 320 alphanumeric in length.
- Creditor reference information can be used to capture the remittance information and when used then the structure type, structure issuer and structure reference is mandatory.
- Original message name identification in the R messages now will contain the complete version of the original underlying message.
- The proprietary reasons codes TECH, FRAD, AC03 and AM09 in camt.056 and the proprietary codes AC04, AM04, NOAS, NOOR and ARDT in camt.029 are now moved under the reason codes and usage of the additional information now should be based on the allowed reason under the ISO reason codes.
- Element Purpose is now present in the R messages and value must be present if it was present in the original message.
- New sub element party is introduced for all the party role tags - Debtor, Creditor, Ultimate Debtor, Ultimate Creditor. For example: Dbtr\_Nm changed to Dbtr\_Pty\_Nm.
- The element Charges Information sub-element Party is replaced by Agent. As a result, in the pacs.004 Positive Response to Recall ChrgsInf\_Pty\_FinInstnId\_BIC changed to ChrgsInf\_Agt\_FinInstnId\_BICFI.

## RPS SDD Rulebook Changes 2023

The RPS RB change enables the migrating to 2019 version of the ISO 20022 and thus offer the end user the opportunity of using the features under the 2019 version which may not be available under earlier versions of the ISO 20022 standard.

The existing version of the message identifiers is changed to newer version, therefore even the xsd should be replaced with the newer version in order to support the latest changes.

| Message older version | Message new version |
| --- | --- |
| pacs.003.001.02 | pacs.003.001.08 |
| pacs.002.001.03 | pacs.002.001.10 |
| pacs.004.001.02 | pacs.004.001.09 |
| pacs.007.001.02 | pacs.007.001.09 |
| camt.056.001.01 | camt.056.001.08 |

1. Reference ID's can now contain internal spaces however leading/trailing spaces are not allowed.
2. The element “BIC” (2009 message version) changed to “BICFI” (2019 message version) and the element “BICOrBEI” (2009 message version) changed to “AnyBIC” (2019 message version).
3. LEI is a new sub-element introduced under the organisation identification for debtor, ultimate debtor and ultimate creditor. When organisation identification is used either AnyBIC, LEI or One occurrence of Other must be present. Its is a 20-digit alphanumeric characters value.
4. After the RB change 2023 payment end-users can benefit from the standard delivery of structured address details about the payer and the payee. It consists of Country and TownName(both mandatory) together with one or more of the other structured elements Department, SubDepartment, StreetName, BuildingNumber, BuildingName, Floor, PostBox, Room, PostCode, TownLocationName, DistrictName and CountrySubDivision. The user has the option to capture either Structured or Unstructured address. The current unstructured PostalAddress can be used in combination with country.
5. Creditor reference information can be used to capture the remittance information and when used then the structure type and structure reference is mandatory.
6. Original message name identification in the R messages now will contain the complete version of the original underlying message.
7. Element Purpose is now present in the R messages and value must be present if it was present in the original message.
8. New sub element party is introduced for all the party role tags - Debtor, Creditor, Ultimate Debtor, Ultimate Creditor. For example: Dbtr\_Nm changed to Dbtr\_Pty\_Nm.
9. The element ChargesInformation sub-element Party is replaced by Agent. As a result, in the pacs.002 SDD Reject, the pacs.004 SDD Return/Refund and the pacs.007 SDD Reversal the sub element party will now be sent as agent. ChrgsInf\_Pty\_FinInstnId\_BIC changed to ChrgsInf\_Agt\_FinInstnId\_BICFI.
10. The proprietary reasons codes TECH, FRAD in camt.056 are now moved under the ISO reason codes.

## RPSSCL SEPA 2025 Credit Transfer and Direct Debit Rulebook changes

The RPSSLC SCT and SDD clearing solution is now fully compliant with the 2025 rulebook changes. Following are the key updates for Credit Transfers and Direct Debits:

- **Ultimate Debtor and Debtor<Org ID>:** For all SCT and SDD message types, the Organisation Identification sub-element under Ultimate Debtor and Debtor must include AnyBIC and LEI, and may contain one occurrence of ‘Other’.
  This is applicable for SCT messages (pacs.008, pacs.004, pacs.028, camt.056, camt.029, camt.087, camt.027, pacs.002S2) and SDD messages (pacs.003, pacs.007, pacs.004, pacs.002, camt.056).
- **Hybrid Postal Address Support:** Debtor and Creditor elements support Hybrid Postal Address. *Town* and *Country* are mandatory, and at least one address line is supported.
  This is applicable for SCT messages (pacs.008, pacs.004, pacs.028, camt.056, camt.029, camt.087, camt.027, and pacs.002S2) and SDD messages (pacs.003, pacs.007, pacs.004, pacs.002, and camt.056).
- **Clearing Directory File format:** The Clearing Directory File Upload process supports the new reach file format (rocs.001.001.07).
  This is applicable for pacs.008 and pacs.004.
- **Recall and RFRO Process:** Under SEPA 2025 standards, EPC has introduced new restrictions due to which, the Originator PSP cannot send a second recall or RFRO for the same SEPA Credit Transfer in either of the following cases:
  - Before the beneficiary bank responds to the initial request
  - After the beneficiary bank sends a negative response (camt.029).

  If there is no response from the Beneficiary PSP even after the recall or RFRO time-out, the Originator may only send a Request for Status Update (pacs.028) and must not initiate another recall or RFRO under any circumstances.

  This change is applicable for the camt.056 SCT message type.
- **Allowed Days for Refund of Direct Debits:** To prevent rejections by other clearing houses, SEPA-Clearer validates the interbank settlement date (ISD) in R-transactions (after settlement – pacs.007 and pacs.004) against the ISD of the original transaction. If the original ISD is older than 440 calendar days for CORE or older than 3 TARGET business days for B2B, the R-transaction is rejected with technical error code DT01.
  This is applicable for the pacs.007 and pacs.004 SDD message types.
- **New Rejection Codes:** A new file level error code’ ECN’ can occur in the following fields for file level rejects by clearing.
  - BBkCVFBlkCdtTrf/FileRjctRsn
  - BBkDVFBlkDirDeb/IdfErrCd
  - BBkQVFBlkCdtTrf/FileRjctRsn

  This is applicable for both the SDD and SCT Clearings.

  - At bulk level for SDD and SCT, the error code ‘B33’ is added.
  - Error code XT78 added for pacs.007.
  - For pacs.002 (COR/B2B), pacs.007 (COR/B2B), and pacs.028 (SCT), incase of R -Transactions, the error code ‘B33’ (OrgnlMsgNmeID) is raised instead of the previous XT33.
- **Support for Verification of Payee (VOP) checks in Credit Transfers:** The RPSSCL POA Product version allows setting up *VOP Check* as ‘Yes’ or ‘No’ for the outward credit transfers.
  Verification of Payee is a key IPR requirement. Temenos provides VOP as a separate module (PPVOFP) outside PPEINS. This module verifies the Payee before payment initiation by sending the Account Number and Payee’s Account Name or ID (as known to the Payer) to an external VOP service provider, which confirms if the name or ID matches the Account Number in the Payee’s bank records.

In this topic

- [Introduction to German Bundesbank RPSSCL Clearing](#IntroductiontoGermanBundesbankRPSSCLClearing)

- [Rulebook Changes for RPSSCL](#RulebookChangesforRPSSCL)
- [RPSSCL CT Rulebook change 2023](#RPSSCLCTRulebookchange2023)
- [RPS SDD Rulebook Changes 2023](#RPSSDDRulebookChanges2023)
- [RPSSCL SEPA 2025 Credit Transfer and Direct Debit Rulebook changes](#RPSSCLSEPA2025CreditTransferandDirectDebitRulebookchanges)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:21:28 PM IST