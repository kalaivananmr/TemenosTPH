# Introduction to Sri Lanka Interbank Payment System (SLIPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SriLanka/Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Sri Lanka > [Sri Lanka Interbank Payment System](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm) > Introduction

- Sri Lanka;)
  - [Sri Lanka Clearing Sri Lanka Clearing](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm)
  - [Sri Lanka Cheques Sri Lanka Cheques](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm)
  - [Sri Lanka Interbank Payment System Sri Lanka Interbank Payment System](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm)
    - [Introduction](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm)
    - [Configuration](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Configuring.htm)
    - [Working with](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Working_with.htm)
    - [Tasks](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Tasks.htm)
    - [Outputs](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Outputs.htm)
  - [Sri Lanka CEFTS Instant CT Payments Sri Lanka CEFTS Instant CT Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm)
  - [Sri Lanka CEFTS Instant DD Payments Sri Lanka CEFTS Instant DD Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm)

Payments

# Introduction to Sri Lanka Interbank Payment System (SLIPS)

Updated On 06 October 2022 |
 3 Min(s) read

Feedback
Summarize

Sri Lanka Interbank Payment System (SLIPS) is a domestic electronic payment system operated by LankaClear (LCPL), which allows batch processing of payments. It accepts payment instructions from participants throughout the day in multiple clearing cycles from Monday to Friday. It supports inward and outward returns, and can be used to send payments to beneficiaries (Credit Transfers) or collect payments from payers (Direct Debits). The SLIPS are used for the following:

- Setup monthly Direct Debit (DD) to pay insurance premium and other utility bills
- Perform salary and welfare payments
- Transfer funds between the bank accounts

The workflow in SLIPS clearing is as follows:



1. Temenos Payments Hub receives the request to process DD and CT transactions. The request can come from an external customer channel or a manual record that can be created from Payment Order or Order Entry versions for capturing the record for CT or DD transaction.
2. The system processes the transaction and if the beneficiary is not in Temenos Payments Hub, an outgoing file is generated and sent to the clearing based on the channel cut-off configured in the system.
3. The clearing forwards the presentation file to the other bank to process the payments sent in the presentation file.
4. Temenos Payments Hub can also receive the presentation file (that includes records for CT,DD and return transactions) from LankaClear.
5. The system processes the transactions after receiving the Inward File system.
6. The outward SLIPS file is generated along with enriched local field *Security Check* with value received from the L3 team.

The following are the files types in SLIPS scheme:

| File Type | Description |
| --- | --- |
| Outward SLIPS | Used by sending bank to send the following:  - Credit Transfer (CT) request - Direct Debit (DD) request - Outward returns to LankaClear - Outward SLIPS file generated with the *Security Check* field (6 digit) |
| Inward SLIPS | Used by receiving bank to receive the following:  - CT request - DD request - Inward returns from LankaClear |

## Illustrating Model Parameters

To know more on parameter setup for SLIPS, Credit Transfer (CT), Direct Debit (DD), refer the [Payment Hub (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm), [Payment Suite (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

PPLNCL provide the facility to send and receive domestic CT and DD transfer SLIPS.

In this topic

- [Introduction to Sri Lanka Interbank Payment System (SLIPS)](#IntroductiontoSriLankaInterbankPaymentSystemSLIPS)

- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:44:15 PM IST