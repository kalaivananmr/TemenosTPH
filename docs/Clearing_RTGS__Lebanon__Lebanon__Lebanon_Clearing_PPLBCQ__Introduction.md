# Introduction to Lebanon Cheque Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Lebanon/Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Lebanon > [Lebanon Cheque Clearing](../../Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm) > Introduction

- Lebanon;)
  - [Lebanon RTGS Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
  - [Lebanon Cheque Clearing Lebanon Cheque Clearing](../../Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm)
    - [Introduction](../../Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm)
    - [Configuration](../../Lebanon/Lebanon_Clearing_PPLBCQ/Configuration.htm)
    - [Working with](../../Lebanon/Lebanon_Clearing_PPLBCQ/Working_with.htm)
    - [Tasks](../../Lebanon/Lebanon_Clearing_PPLBCQ/Tasks.htm)
    - [Outputs](../../Lebanon/Lebanon_Clearing_PPLBCQ/Outputs.htm)

Payments

# Introduction to Lebanon Cheque Clearing

Updated On 22 March 2025 |
 2 Min(s) read

Feedback
Summarize

This section gives an introduction to Lebanon Cheque Clearing.

## Inward Cheque Clearing

Temenos Payments Hub (TPH) can do the following:

- Receive, validate and process a flat (fixed length) file from the clearing house with the inward clearing cheques. This is a part of the Lebanon inward cheque clearing.
- Support a return file (flat file in the Lebanon cheque clearing format), which is generated for the returned inward clearing cheques.
- Additionally, in the Repair page for cheque debit payments, if the user decides to return the payment with a reason code, the system can be configured to take charges for the return payment. The user can waive the return fee when returning a cheque payment.
- Configure to define a threshold amount to qualify an inward clearing cheque payment. If the amount exceeds the payment, it is then placed in the Repair queue.

## Outward Cheque Clearing

Teller Financial Services page is used to capture the input of multiple local outward clearing cheques, which are deposited for collection. Alternatively, TPH can generate a flat file with the details of deposited outward cheques. This file is in the Lebanon cheque clearing format and can be sent to the clearing to receive a response. On receiving the response file from clearing for returns, it is validated and processed in TPH. These cheques are updated to Returned or Cleared.

The user can also manually update the cheque status (using fast path enquiry)  as Cleared or Returned.

## Illustrating Model Parameters

To know more on parameter setup for Lebanese Cheques, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

Lebanese Cheques module can process both outward and inward cheque clearing payments.

In this topic

- [Introduction to Lebanon Cheque Clearing](#IntroductiontoLebanonChequeClearing)

- [Inward Cheque Clearing](#InwardChequeClearing)
- [Outward Cheque Clearing](#OutwardChequeClearing)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:14:02 PM IST