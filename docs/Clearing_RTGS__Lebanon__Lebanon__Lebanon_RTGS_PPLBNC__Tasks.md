# Tasks for Lebanon RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Lebanon/Lebanon/Lebanon_RTGS_PPLBNC/Tasks.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Lebanon > [Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm) > Tasks

- Lebanon;)
  - [Lebanon RTGS Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
    - [Introduction](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
    - [Configuration](../../Lebanon/Lebanon_RTGS_PPLBNC/Configuration.htm)
    - [Working with](../../Lebanon/Lebanon_RTGS_PPLBNC/Working_with.htm)
    - [Tasks](../../Lebanon/Lebanon_RTGS_PPLBNC/Tasks.htm)
    - [Outputs](../../Lebanon/Lebanon_RTGS_PPLBNC/Outputs.htm)
  - [Lebanon Cheque Clearing Lebanon Cheque Clearing](../../Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm)

Payments

# Tasks for Lebanon RTGS

Updated On 22 March 2025 |
 2 Min(s) read

Feedback
Summarize

Lebanon RTGS is a real time gross settlement payment system. It processes each RTGS payment initiated on an individual basis and settles it immediately.

## Workflow

In Lebanon RTGS, the user can perform the below tasks:

[Initiating Lebanese RTGS Payments](#)

The Lebanese RTGS payments are initiated through order entry in Temenos Payments Hub (TPH).

To initiate a Lebanese RTGS payment transaction, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate Customer Transaction** > **Outgoing Transfer**.
2. In the Order Entry Outgoing Transfer (CTR) screen, enter values in the following fields:

- *Transaction Amount*
- *Transaction Currency*
- *Receiver Institution*

3. In the Debit Credit Info tab, enter values in the following fields:

- *Debit Account Number*
- *Beneficiary Account*
- *Beneficiary Name*

4. In the Routing Information tab, enter a value in the *Account With Institution* field.
5. Click the **Validate** icon to check for errors and overrides.

After successful validation of the transaction, *Output Channel* field is defaulted with the value LBRTGS along with the credit side information provided.

6. Click the **Commit** icon.

The transaction is committed and sent for authorisation.

[Authorising Lebanese RTGS Payments](#)

The Lebanese RTGS payments that are initiated must be approved for further processing.

To authorise a Lebanese RTGS payment transaction, follow the below steps:

| SCREENS | WORKFLOW |
| --- | --- |
|  | 1. Log in as **PAYUSER2** > **Payment Hub** > **Payment Approvals** > **Authorise Pending Payments** > **Authorise OrderEntry & Repair Payments** > **Pending Authorise Payments**. |
| Pending Authorise Payments | 2. Click the **Auth** icon corresponding to a record. |
| Authorise Screen | 3. Verify the details and then click the **Authorise** icon.  The transaction is authorised. |

In this topic

- [Tasks for Lebanon RTGS](#TasksforLebanonRTGS)

- [Workflow](#Workflow)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:14:00 PM IST