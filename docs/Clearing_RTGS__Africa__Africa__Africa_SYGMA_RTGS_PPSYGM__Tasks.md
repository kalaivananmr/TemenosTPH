# Tasks for SYGMA RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYGMA_RTGS_PPSYGM/Tasks.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm) > Tasks

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
    - [Introduction](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
    - [Configuration](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Configuration.htm)
    - [Working with](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Working_with.htm)
    - [Tasks](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Tasks.htm)
    - [Outputs](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Outputs.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Tasks for SYGMA RTGS

Updated On 07 August 2023 |
 3 Min(s) read

Feedback
Summarize

SYGMA (Système des gros montants automatisé) is a Real time gross settlement system launched in the Central bank of Central African States.

## Workflow

The user can perform the following activities:

[Initiating SYGMA RTGS Payment](#)

SYGMA RTGS payments are initiated through payment orders based on the inputs provided by the user or also imposed by the user in Temenos Payments Hub (TPH).

To initiate a new SYGMA RTGS transaction, follow the below steps:

| SCREENS | WORKFLOW |
| --- | --- |
|  | 1. Log in as **PAYUSER1** > **Payment Order** > **Input Payment Order** > **Africa** > **SYGMA RTGS**. |
| Contract Screen | 2. Click the **New** icon. |
| SYGMARTGS | 3. Enter values in the following fields:  - *Payment Currency* - *Payment Amount* - *Debit Account Number*  4. In the Beneficiary Details tab, enter values in the following fields:  - *Beneficiary ID* - *Beneficiary Account No* - *Beneficiary Name*  5. In the Routing Details tab, enter a value in the *Account with Bank Clearing Code* field.  Output channel is set to SYGMA along with credit side information such as Credit Account Number, Credit Account Currency based on the debit side information and routing information. Channel SYG is determined based on the R&S contract configured for the routing product assigned for such payments. 6. Click the **Commit** icon.  The transaction is committed and transaction reference is created and sent for authorisation. |

[Authorising, Deleting or Viewing SYGMA RTGS Payments](#)

The SYGMA RTGS payments that are initiated must be approved for further processing. The payments must be approved in TPH.

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

- [Tasks for SYGMA RTGS](#TasksforSYGMARTGS)

- [Workflow](#Workflow)

Related topics:

- [Receive and Execute Outward Remittance](/docs/Processes/Reference_Processes/m9dbd8011-594c-11ea-73c9-005056b05354_gfx.htm)
- [Payment Hub Processes](https://tlcengine.temenos.com/Content/MarkedId/873447CA-2482-445F-8373-09AA9AF4BCF7)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:33:46 PM IST