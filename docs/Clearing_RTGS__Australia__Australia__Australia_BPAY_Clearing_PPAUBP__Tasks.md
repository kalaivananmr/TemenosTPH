# Tasks for BPAY Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Australia/Australia/Australia_BPAY_Clearing_PPAUBP/Tasks.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Australia > [BPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm) > Tasks

- Australia;)
  - [BPAYBPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
    - [Introduction](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
    - [Configuration](../../Australia/Australia_BPAY_Clearing_PPAUBP/Configuration.htm)
    - [Working with](../../Australia/Australia_BPAY_Clearing_PPAUBP/Working_with.htm)
    - [Tasks](../../Australia/Australia_BPAY_Clearing_PPAUBP/Tasks.htm)
    - [Outputs](../../Australia/Australia_BPAY_Clearing_PPAUBP/Outputs.htm)
  - [BECSBECS](../../Australia/Australia_BECS_PPBECS/Introduction.htm)
  - NPP Payments;)
  - BPAY Agency Banking;)
  - AURTGS Clearing;)
  - DE (BECS) Agency Banking;)
  - Clearing Directory Upload and Reachability Check;)

Payments

# Tasks for BPAY Clearing

Updated On 07 August 2025 |
 3 Min(s) read

Feedback
Summarize

BPAY is an electronic bill payment system in Australia which enables the payments to be made through a financial institution's online, mobile or telephone banking facility to organisations which are registered as BPAY billers.

The businesses registered with BPAY will be allocated a biller number. The customers making payment need to log into their bank’s portal and input the biller code, customer reference number and the transaction amount. Once the clearing validations are successful, then the customer’s bank transfers the funds electronically to the biller’s bank.

## Workflow

In BPAY Clearing Australia, the user can perform the following activities:

[Initiating BPAY Payment](#)

BPAY payments are initiated through payment orders based on the inputs provided by the user or also imposed by the user in Temenos Payments Hub (TPH).

To initiate BPAY payment transaction, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Order** > **Input Payment Order** > **Australia** > **BPAY**.
2. In the Bill Payments BPAY Australia screen, enter values in the following fields:

- *Payment Currency*
- *Payment Amount*
- *Debit Account Number*
- *Beneficiary ID*
- *Biller code*

3. Click the **Validate** icon to check for errors and overrides.
4. Click the **Commit** icon.

The transaction is committed and transaction reference is created and sent for authorisation.

[Authorising, Deleting, Viewing BPAY Payments](#)

The BPAY payments that are initiated must be approved for further processing. The payments must be approved in TPH.

To authorise a transaction, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Order Menu** > **Authorise/Delete Payment Order** > **Authorise/Delete Payment Order**.
2. In the Payment Order Unauthorised List screen, click the **Authorise** icon corresponding to a record.
3. In the Payment Order New screen, verify the details and then click the **Authorise** icon.

The transaction is authorised.

To delete a transaction, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Order Menu** > **Authorise/Delete Payment Order** > **Authorise/Delete Payment Order**.
2. In the Payment Order Unauthorised List screen, click the **Delete** icon corresponding to a record.
3. In the Payment Order New screen, click the **Delete** icon.

The transaction is deleted.

To view a transaction, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Order Menu** > **Authorise/Delete Payment Order** > **Authorise/Delete Payment Order**.
2. In the Payment Order Unauthorised List screen, click the **View** icon corresponding to a record.

The Payment Order New screen displays the record in view mode.

In this topic

- [Tasks for BPAY Clearing](#TasksforBPAYClearing)
  - [Workflow](#Workflow)

Related topics:

- [Receive and Execute Bill Payment](https://tlcengine.temenos.com/Content/MarkedId/5544C396-2795-4293-83D7-E75FE7C16116)
- [Payment Hub Processes](https://tlcengine.temenos.com/Content/MarkedId/873447CA-2482-445F-8373-09AA9AF4BCF7)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:21:51 PM IST