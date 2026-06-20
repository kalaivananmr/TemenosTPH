# Introduction to SIC - Instant Payment

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_SIC-IP/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm) > Introduction

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
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
    - [Introduction](../../Europe/Europe_SIC-IP/Introduction.htm)
    - [Configuration](../../Europe/Europe_SIC-IP/Configuration.htm)
    - [Working With](../../Europe/Europe_SIC-IP/WorkingWith.htm)
    - [Tasks](../../Europe/Europe_SIC-IP/Tasks.htm)
    - [Outputs](../../Europe/Europe_SIC-IP/Outputs.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to SIC - Instant Payment

Updated On 23 October 2025 |
 21 Min(s) read

Feedback
Summarize

Instant payment is already a reality in many countries. In order to make it possible in Switzerland as well, SIX and the Swiss National Bank have launched a new generation of the central payment infrastructure – the “SIC5” platform – on 17 November 2023.

SIC IP is an Instant settlement clearing system in Switzerland, operated by SIX on behalf of the SWISS National Bank. This clearing ensures that the payer transfers funds to the payee in real time, around the clock (24\*7\* 365).

Through financial institutions participating in the SICIP Service, businesses and individuals will be able to send and receive instant payments conveniently. Recipients will have full access to funds immediately, giving them greater flexibility to manage their money and make time-sensitive payments.

As part of this enhancement, TPH can receive incoming pacs.008 payments from SICIP clearing and do the necessary validation before posting the funds in the client account. TPH also generates pacs.002 ( positive or negative) for the received incoming pacs.008. Based on the incoming pacs.002 (settlement confirmation or cancellation) from SICIP clearing, the payment is either executed or cancelled in TPH. Clients can initiate pacs.028 (status request) for the received incoming pacs.008 as part of this enhancement.

As part of SIC Instant framework, the SIC Instant Liquidity Transfer module helps participant bank to initiate liquidity transfer as pacs.009 to transfer the excess funds from instant clearing account to RTGS clearing account held with SICIP. Based on the incoming pacs.002 (settlement confirmation or cancellation) from SICIP clearing, the payment is either executed or reversed in TPH. The SICIP LTR payment order product supports the generation of pacs.009.

## Outgoing Customer Credit Transfer Payment

The user can initiate Customer Credit Transfer payment through SIC Instant POA version or API and outgoing pacs.008 is generated once validations are successful.

The system supports the below subsequent flows for the outward pacs.008 payment.

- Handling incoming pacs.002 from SIC IP for the underlying outward pacs.008 payment.
- Handling outward pacs.028 for the outward pacs.008.
- Handling incoming pacs.002 acknowledgement for the generated pacs.028 from SIC IP clearing.
- Handling of outward cancellation request camt.056 and its inward negative reject response camt.029 and generation of outward camt.025.
- Handling of outward cancellation request camt.056 and its inward positive response pacs.004 and generation of outward pacs.002.
- Handling of incoming pacs.002 for outward generated pacs.004.

TPH supports SIC IP clearing directory file upload and SIC IP reachability check based on latest V3 file.

## Hybrid Postal Address for Agents and Parties

The Temenos SIC Instant Clearing solution is compliant with the SIC5 Instant rulebook changes for 2025. These changes are applicable for Customer Credit Transfer and Return/Recall messages for Ultimate Debtor, Debtor, Debtor Agents, Ultimate Creditor, Creditor, and Creditor Agents. This impacts all the messages for SIC5 Instant Clearing solution. From November 2025, the following postal address-related changes are applicable:

| Address type | Address Rule |
| --- | --- |
| Structured postal address | As a minimum requirement, the postal address must include the Town Name and Country elements. It cannot contain the Address Line element. |
| Unstructured postal address | The postal address uses only the Address Line element. Three occurrences of the Address Line element with up to 35 characters are allowed. |
| Hybrid (semi-structured) address | A postal address must include the Town Name and Country elements, and it also allows the Address Line element to be included. Two or three (depending on the tags) occurrences of the Address Line element with up to 70 characters are allowed. Other structured elements in addition to Town Name and Country can also be included, for example, Post Code.  It is recommended (no validation performed by RTGS) that the data present in structured elements within the Postal Address must not be repeated in Address Line under any circumstances. |

The timeline below outlines the possible Postal Address options for all Agents and Parties as of Rulebook 2025:

- From November 2025 to November 2026, SIX permits semi-structured (hybrid), fully structured, or fully unstructured postal addresses.
- From November 2026, SIX permits a semi-structured (hybrid) or fully structured postal address. Fully unstructured postal addresses will no longer be permitted. The usage of the unstructured Address Line as a standalone element within Postal Address will not be supported after November 2026.

[Beneficiary Application](#)

This table illustrates the address details that are captured in the Beneficiary application and their mapping to Payment Order Product (POA) or TPH ISO Order Entry screen during payment initiation and the enhancement to the system.

| Agents or Parties | System Impact (Yes or no) | Beneficiary Application |
| --- | --- | --- |
| Creditor | Yes | Currently, the user can enter only a structured address.  The system is to be enhanced to allow the user to enter unstructured address lines and to raise a warning if town name or country is not entered. |
| Creditor Agent | Yes (POA) | Currently, the user can enter only a structured address and there is no validation in the application.  The system is to be enhanced to allow the user to enter unstructured address lines and to raise a warning if town name or country is not entered. |
| Ultimate Creditor | Yes (POA) | Currently, the user can enter a structured address, an unstructured address, or both, and there is no validation in the application.  The system is to be enhanced to raise warning if town name or country is not entered. |
| Ultimate Debtor | Yes (POA) | Currently, the user can enter a structured address, an unstructured address, or both, and there is no validation in the application.  The system is to be enhanced to raise warning if town name or country is not entered. |

- During Payment Initiation through POA, structured address from the Beneficiary application is copied to Payment order product. The system will be enhanced to copy unstructured address from the Beneficiary application.
- During Payment Initiation through TPH, OE Initiation is not applicable for Instant payments.

[Payment Order Application](#)

The table below illustrates the behavior of the address lines fields in POA for a SIX product (customer transfer and bank transfer).

| Agents or Parties | System Impact(Yes or no) | Description |
| --- | --- | --- |
| Debtor | Yes | When the debtor details are imposed by the user, the following validations are performed (warning is raised). Town Name and Country is mandatory if:   - Only a structured address is entered - Both structured and unstructured addresses are entered   There is currently no validation on the length and number of lines for unstructured address lines entered by the user. This continues to apply when a hybrid address is entered.  When the debtor details are not imposed by the user, the structured address present in the T24 customer application is retrieved and stored as part of the payment order. The system is enhanced to retrieve unstructured address from the customer application. |
| Creditor and Creditor Agent | Yes | Town Name and Country is mandatory (warning is raised) if:   - Only a structured address is entered - Both structured and unstructured addresses are entered   There is currently no validation on the length and number of lines for unstructured address lines entered by the user. This continues to apply when a hybrid address is entered. |
| Ultimate Creditor and Ultimate Debtor | Yes | Town Name and Country is mandatory (warning is raised) if:   - Only a structured address is entered - Both structured and unstructured addresses are entered   Entering only an unstructured address is not allowed.  There is currently no validation on the length and number of lines for unstructured address lines entered by the user. This continues to apply when a hybrid address is entered. |
| Invoicer, Invoicee, Garnishee, and Garnishment Administrator | No | These fields are not available in the payment order application and hence should not be used in the SIC5 Instant payment messages. |

[Sender FI](#)

The table below describes the impact where TPH is acting as Sender FIs as the direct participant for a payment originated by DP’s customer (outgoing).

**For message type: pacs.004**

| Agents or Parties | System Impact | Description |
| --- | --- | --- |
| Debtor Agent and Creditor Agent | Yes | Currently in the ISO Order Entry Return Screen (Customer transfer), the user is allowed to enter structured and unstructured address lines in addition to either fully structured or unstructured addresses. For returns generated by the system, the details from the original payment are copied to the return payment (reverse role mapping).   - If both structured address (minimum town and country) and unstructured address details are present for the debtor agent, the hybrid address is populated in the outgoing pacs.008 message to SIX. - When a hybrid address is populated, the system must ensure that only a maximum of two address line occurrences (each having a maximum length of 70) are present. - If there are more than 140 characters of unstructured address line details in addition to the structured address (with town name and country), only 140 characters are sent out with 70 characters each in the two address lines tag elements.   Currently, when an address is present, the system does not validate the existence of only structured or unstructured addresses. The only validation that is being performed is that if only a structured address is present, Town Name and Country is mandatory (an error is raised). The system is to be enhanced to validate whether a hybrid address is present. If yes, Town Name and Country is mandatory for order entry and repair payments (warning is raised). |
| Charge Information or Agent | No | There is no field in the Order Entry Return screen. For the fees calculated by TPH, the TPH Company BIC is populated in the outgoing pacs.004. |
| Creditor | Yes | Currently in the ISO Order Entry Return Screen (Customer transfer), the user is allowed to enter structured and unstructured address lines in addition to either fully structured or unstructured addresses.   - If only structured address is entered, Town Name and Country are mandatory. - In case of hybrid address, Town Name and Country are to be made mandatory. - If both structured address (minimum town and country) and unstructured address details are present for the creditor, the hybrid address is populated in the outgoing pacs.008 message to SIX. - When a hybrid address is populated, the system must ensure that only a maximum of two address line occurrences (each having a maximum length of 70) are present. - If there are more than 140 characters of unstructured address line details in addition to the structured address (with town name and country), only 140 characters are sent out with 70 characters each in the two address lines tag elements.   Currently, when an address is present, the system does not validate the existence of only structured or unstructured addresses. The only validation that is being performed is that if only a structured address is present, Town Name and Country is mandatory (an error is raised). The system is to be enhanced to validate whether a hybrid address is present. If yes, Town Name and Country is mandatory for order entry and repair payments (warning is raised). |
| Debtor | Yes | Currently in the ISO Order Entry Return Screen (Customer transfer), when the debtor details are imposed by the user, the system allows the user to enter structured and unstructured address lines in addition to either fully structured or unstructured addresses.   - If only structured address is entered, Town Name and Country are mandatory. - In case of hybrid address, Town Name and Country are to be made mandatory. - If both structured address (minimum town and country) and unstructured address details are present for the debtor (imposed and not imposed by user), the hybrid address is populated in the outgoing pacs.008 message to SIX. - When a hybrid address is populated, the system must ensure that only a maximum of two address line occurrences (each having a maximum length of 70) are present. - If there are more than 140 characters of unstructured address line details in addition to the structured address (with town name and country), only 140 characters are sent out with 70 characters each in the two address lines tag elements. - When the debit customer is validated with the account and customer database, the unstructured address (stored in the customer database) is stored in the system to accommodate the two lines each having a maximum length of 70 characters. These details can be viewed in the order entry, repair, or view screens of the payment transaction.   Currently, when an address is present, the system does not validate the existence of only structured or unstructured addresses. The only validation that is being performed is that if only a structured address is present, Town Name and Country is mandatory (an error is raised). The system is to be enhanced to validate whether a hybrid address is present. If yes, Town Name and Country is mandatory for order entry and repair payments (warning is raised).  The above details are applicable for embedded and standalone (TPH). For standalone, the customer database can be in a different instance of T24, Microservice, or external Core. |
| Ultimate Debtor and Ultimate Creditor | Yes | Currently in the ISO Order Entry Return Screen (Customer transfer), the user is allowed to enter structured and unstructured address lines in addition to either fully structured or unstructured addresses. For returns generated by the system, the details from the original payment are copied to the return payment (reverse role mapping).   - If both structured address (minimum town and country) and unstructured address details are present for the ultimate debtor in the payment instruction, the hybrid address is populated in the outgoing pacs.008 message to SIX. - When a hybrid address is populated, the system must ensure that only a maximum of two address line occurrences (each having a maximum length of 70) are present. - If there are more than 140 characters of unstructured address line details in addition to the structured address (with town name and country), only 140 characters are sent out with 70 characters each in the two address lines tag elements.   The system is to be enhanced to validate:   - If only a structured address is present, Town Name and Country is mandatory (warning is raised). - When a hybrid address is present, Town Name and Country is mandatory for order entry and repair payments (warning is raised).   Only structured address or hybrid address is allowed. Fully unstructured address is not allowed. |
| Initiating Party | No | TPH does not populate initiating party for an outgoing return, hence this tag must not be used. |
| Originator | Yes | If the return is originated by the bank on behalf of customer request, the address details received for the original beneficiary is populated in the originator tag element.  If structured address (minimum town and country) and unstructured address details are present in the payment instruction, the hybrid address is populated in the outgoing pacs.004 message to SIX.  When the hybrid address is populated, the system must ensure that only a maximum of two address line occurrences (each having a maximum length of 70) are  present. |

**For message types: camt.056, camt.029**

| Agents or Parties | System Impact(Yes or No) | Description |
| --- | --- | --- |
| Originator | Yes | Outward – Recalls: The system sends the hybrid, structured, or unstructured address depending on what is available in the underlying payment.  Outward – ROI: The system sends the hybrid, structured, or unstructured address depending on what is available in the recall received,  - The above details are applicable for embedded and standalone (TPH). For standalone, the customer database can be in a different instance of T24, Microservice, or external Core. - Only structured address or hybrid address is allowed. Fully unstructured address is not allowed. |

- The ISO Order Entry screen is not considered, as this screen should not be used for initiating Instant payments.
- Liquidity transfer pacs.009 is not in scope for the hybrid address change.

[Receiver FI](#)

The table below describes the impact where TPH is acting as a receiving FI, and the customer is ‘On Us’. The direction of the payment is ‘Incoming’.

| Agents or Parties | Message Types | System Impact(Yes or No) | Gap Details |
| --- | --- | --- | --- |
| Debtor Agent \* | Pacs.008, pacs.004 | No | In the Order Entry Screen, the user can enter structured address and unstructured lines in addition to a fully structured address or a fully unstructured address. There is no validation as these messages are received from the clearing and keyed in manually.  The address details (structured and unstructured) received in the payment instruction are stored in the system and displayed on the screen accordingly. This continues for hybrid address and there is no impact on the incoming payment. |
| Creditor Agent \* | Pacs.008, pacs.004 |
| Charge Information/Agent | Pacs.008, pacs.004 | No | Charge Agent details are not present in the OE incoming CTR screen.  The address details (structured and unstructured) received in the payment instruction are stored in the system but not displayed on the screen. This continues for hybrid address and there is no impact on the incoming payment. |
| Creditor | Pacs.008, pacs.004 | No | In the Order Entry Screen, the user can enter structured address and unstructured lines in addition to a fully structured address or a fully unstructured address. There is no validation as these messages are received from the clearing and keyed in manually.  The address details (structured and unstructured) received in the payment instruction are currently stored in the system and displayed on the screen accordingly. This continues for hybrid address and there is no impact on the incoming payment. |
| Debtor |
| Ultimate Debtor | Pacs.008, pacs.004 |
| Ultimate Creditor |
| Initiating Party | Pacs.008, pacs.004 | No | Not applicable for SIC5 Instant. |
| Originator | pacs.004, pacs.002 | No | For pacs.004, the address details (structured and unstructured) received in the payment instruction are currently stored in the system but not displayed on the screen. This continues for hybrid address and there is no impact on the incoming payment.  For pacs.002, the address details are not stored in the system and hence there is no impact. |
| Creator | Camt.056, camt.029 | No | Not applicable for SIC5 Instant |
| Originator | Camt.056, camt.029 | No | The address details (structured and unstructured) received in the recall and resolution of investigation messages are currently stored in the system and displayed on the screen. This continues for hybrid address and there is no impact on the incoming payment. |

- \*For Agents, only the Town Name, Post Code, and Country details of the structured address details are displayed.
- There is no Order Entry Incoming screen for pacs.004 and pacs.008.

In this topic

- [Introduction to SIC - Instant Payment](#IntroductiontoSICInstantPayment)

- [Outgoing Customer Credit Transfer Payment](#OutgoingCustomerCreditTransferPayment)
- [Hybrid Postal Address for Agents and Parties](#HybridPostalAddressforAgentsandParties)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:21:49 PM IST