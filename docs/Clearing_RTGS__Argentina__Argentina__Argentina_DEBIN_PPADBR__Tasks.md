# Tasks for DEBIN Registration Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Argentina/Argentina/Argentina_DEBIN_PPADBR/Tasks.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Argentina > DEBIN Registration Clearing > Tasks

- Argentina;)
  - DEBIN Registration Clearing;)
    - [Introduction](../../Argentina/Argentina_DEBIN_PPADBR/Introduction.htm)
    - [Configuration](../../Argentina/Argentina_DEBIN_PPADBR/Configuration.htm)
    - [Working with](../../Argentina/Argentina_DEBIN_PPADBR/Working_with.htm)
    - [Tasks](../../Argentina/Argentina_DEBIN_PPADBR/Tasks.htm)
    - [Outputs](../../Argentina/Argentina_DEBIN_PPADBR/Outputs.htm)
  - CT & DD (ACH) Clearing;)
  - Instant Clearing;)

Payments

# Tasks for DEBIN Registration Clearing

Updated On 07 August 2023 |
 3 Min(s) read

Feedback
Summarize

Argentina Immediate Transfer is an instant payment method helps to process the payment immediately and available around the clock, throughout the year.

## Workflow

In DEBIN (Immediate Debit), the user can perform the following activities:

[Initiating an Argentina Immediate Transfer Payment](#)

Argentina Immediate Transfer payments are initiated through Payment Order based on the inputs given by the user or also imposed by user in Temenos Payments Hub.

To initiate a payment order, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Order** > **Input Payment Order** > **Argentina** > **Immediate Transfer**.
2. In the Payment Order - Argentina Local Immediate screen, enter values in the following fields:

- *Payment Currency*
- *Payment Amount*
- *Payment Execution Date*
- *Ordering Customer Alias or CBU*
- *Purpose Proprietary*
- *Beneficiary ID*
- *Debit Currency*

3. Click the **Validate** icon to check for errors and overrides.

Output channel is set to ARG along with credit side information such as Credit Account Number, Credit Account Currency based on the debit side information and routing information. Channel ARG is determined based on the R and S contract configured for the routing product assigned for such payments.

4. Click the **Commit** icon.

The transaction is committed and transaction reference is created and sent for authorisation.

[Authorising, Deleting or Viewing the Argentina Immediate Transfer Payments](#)

The Argentina Immediate Transfer payments that are initiated must be approved for further processing. The payments must be approved in Temenos Payments Hub.

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

- [Tasks for DEBIN Registration Clearing](#TasksforDEBINRegistrationClearing)

- [Workflow](#Workflow)

Related topics:

- [Execute Immediate Transfer](https://tlcengine.temenos.com/Content/MarkedId/1B0FE805-DB20-4BD2-B60F-AB10C9D7D3A7)
- [Payment Hub Processes](https://tlcengine.temenos.com/Content/MarkedId/873447CA-2482-445F-8373-09AA9AF4BCF7)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:51:43 PM IST