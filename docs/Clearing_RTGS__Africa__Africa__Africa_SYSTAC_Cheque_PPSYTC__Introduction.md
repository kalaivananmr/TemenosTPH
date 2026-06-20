# Introduction to SYSTAC Cheque Payment

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm) > Introduction

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
    - [Introduction](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
    - [Configuring](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Configuration.htm)
    - [Working with](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Working_with.htm)
    - [Tasks](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Tasks.htm)
    - [Outputs](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Outputs.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Introduction to SYSTAC Cheque Payment

Updated On 23 May 2023 |
 6 Min(s) read

Feedback
Summarize

The ‘Système de Télécompensation en Afrique Centrale’ (SYSTAC) is a net, secure and automated system that processes large volume non-emergency debit and credit transactions (credit transfers and cheques) with a unit amount of less than CFA 100 million. It has the following objectives in Central Africa:

- Fast processing of transactions in accordance to Bank of Central African States (BEAC) and international standards
- Reducing risks associated to payment transactions
- Facilitating monetary management and functioning of the financial market
- Making exchanges at national and sub-regional level

Additionally, SYSTAC is dedicated to clearing financial flows at the regional level (CEMAC).

## SYSTAC Participants

BEAC provides participant’s details to each bank, and when there is a change in the participant repository it generates a new file and circulates to all participants. The text file consists of following details:

- Banks in CEMAC region with bank codes (banque.txt)
- Branches of banks in the above file (agence.txt)

The participant details are uploaded in CA.CLEARING.DIRECTORY and used for the reachability checks.

## Types of Payment and Messages

The following are the message and file types for cheque:

| File or Message Type | Description |
| --- | --- |
| DATA | Details of the file for outward cheque collection (which is handled locally) |
| ENV | File generated to clearing |
| RCP | File received from clearing |
| 30-21 | Presentation of normal cheques |
| 33-21 | Presentation of the re-presented cheques |
| 30-22 | Return of normal cheques |
| 33-22 | Return of re-presented cheques |

The below workflow diagram shows the process of cheque collection and DDA.






## SYSTAC Cut-Off Time

BEAC cut-off time for outward (ENV) file is 11:45. The bank start receiving inward (RCP) file from 13:45.

## Outward Cheque Collection

SYSTAC has the following types of outward cheque collection:

| Outward Cheque Collection | Description |
| --- | --- |
| Outward cheque presentation | When the TPH customers provide the cheque of other banks, it is sent to the respective banks for clearing (through SYSTAC clearing). This is known as outward cheque collection.TPH bank processes an outward cheque collection as follows:  - Uploads the data of the outward cheques to the Teller module and passes it to TPH for further processing (with an indicator that the cheques is presented or re-presented). - Uses the data and processes it in STP mode based on all the business validation, which includes reachability checks. - Generates outward file to clearing at the clearing frequency. - Raises settlement entries during the generation of the outward file (pre-settle) - Makes an API call to the Cheque module to update the cheque status. |
| Cancellation of outward cheque presentation | This enables to cancel all the outward cheque collection transactions awaiting to be sent to clearing.  - Initiate the cancellation (manually) by using an enquiry. - Enter the reason to complete the cancellation. This removes the transaction from the out file queue. |
| Reject of cheque presentation by clearing | This helps to accept and map the outward file rejected by clearing (automatically) to TPH.  - Identifies and reverses the original transaction. - Makes an API call to the Cheque Collection module to update the cheque status. |
| Reject of cheque presentation by other bank | This allows to accept and map the inward return file received from clearing (automatically) to TPH.  - Creates and completes the return transaction. - Identifies and completes the original transaction with return. - Makes an API call to Cheque Collection module to update the cheque status. |

## Inward Cheque Clearing

SYSTAC has the following types of inward cheque clearing:

| Inward Cheque Clearing | Description |
| --- | --- |
| Inward cheque presentation | This helps to accept and map the file having inward cheques to TPH.  - Processes as STP and completes it.  If an error is encountered, it moves the transaction to the Repair queue for manual intervention. - Raises settlement entries during the time of loading the file (Pre-settle). - Validates the cheque details against CHEQUE.REGISTER.SUPPLEMENT application. |
| Reject cheque presentation by TPH | This displays all inward cheques in an enquiry that failed due to validation. The user has to manually initiate return by entering the reject reason code. System performs the following:  - Marks the original transaction as ‘Returned’ - Creates a return transaction and places it in the Out File queue.   The outward return file to clearing is generated at the clearing frequency. |
| Cancellation of reject of inward cheque presentation by TPH | This enables to cancel all the outward return transactions awaiting to be sent to clearing.  - Initiates the cancellation (manually) by using an enquiry. - Enter the reason to complete the cancellation of return transaction. This removes the return transaction from the Out File queue. - Moves the original transaction to Repair queue and the user has to manually accept to complete the transaction. - Makes an API call to the cheque register supplement to update the cheque status. |

## Illustrating Model Parameters

Read the [Temenos Payment (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Suite (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) user guides for information on parameter setup for Cheques and Cheque Returns.

## Illustrating Model Products

This module provides facility to initiate and receive cheque requests through SYTAC Cheque Clearing.

In this topic

- [Introduction to SYSTAC Cheque Payment](#IntroductiontoSYSTACChequePayment)

- [SYSTAC Participants](#SYSTACParticipants)
- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [SYSTAC Cut-Off Time](#SYSTACCutOffTime)
- [Outward Cheque Collection](#OutwardChequeCollection)
- [Inward Cheque Clearing](#InwardChequeClearing)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:33:59 PM IST