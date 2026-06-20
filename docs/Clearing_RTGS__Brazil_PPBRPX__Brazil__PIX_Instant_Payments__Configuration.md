# Configuration

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Brazil_PPBRPX/Brazil/PIX_Instant_Payments/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Brazil > PIX Instant Payments > Configuration

- Brazil;)
  - PIX Instant Payments;)
    - [Introduction](../../Brazil/PIX_Instant_Payments/Introduction.htm)
    - [Configuration](../../Brazil/PIX_Instant_Payments/Configuration.htm)
    - [Working with](../../Brazil/PIX_Instant_Payments/WorkingWith.htm)
    - [Tasks for PIX Instant Payments](../../Brazil/PIX_Instant_Payments/Tasks.htm)
    - [Outputs for PIX Instant Payments](../../Brazil/PIX_Instant_Payments/Outputs.htm)
  - TED Payments;)
  - ACH Payments;)

Payments

# Configuring PIX Instant Payments

Updated On 12 April 2026 |
 4 Min(s) read

Feedback
Summarize

This topic helps the user to perform the required configuration to enable the PIX Instant Payments functionality.

## Pre-Configuration

Temenos performed the following configuration before the user enabling the PIX Instant Payments functionality.

[Dependent War and Property File Changes](#)

The latest irf war for version 7.4 is available in deployments folder.



[TPH Configurations](#)

Ensure the following applications are configured as given in the screenshots:

**VERSION Configuration**

- For PIX Inward transactions, ensure the debit account is configured in the `PAYMENT.ORDER` local version. Sample illustration is given  below using the core version `PAYMENT.ORDER,PI.API.GENERIC.5.7.1`, which is invoked by an API.


- For MED Inward transactions, ensure the debit account is configured in the PAYMENT.ORDER local version (and the API used to call the version to be developed by L3) as shown below.

- For PIX Saque and Troco Inward transactions, ensure the debit account is configured in the PAYMENT.ORDER local version (and the API to call the version to be developed by L3), as shown below.


  For Inward transactions, if the debit account is configured in TPS.INTERNAL.CONFIGS, the debit account defined in the PAYMENT.ORDER version will be overridden.

`TPS.INTERNAL.CONFIGS` **Configuration**

- In the EMBD.PMT.STP record, ensure the POA.INIT.PMT value is updated in the *Value* field.


- Configure the suspense account numbers while creating the PIX record of the TPS.INTERNAL.CONFIGS application for PIX Inward and PIX Outward payments.

- Configure the suspense account numbers while creating the MED record of the TPS.INTERNAL.CONFIGS application for MED Return and MED Return Request.

- Configure the suspense account numbers while creating the PIXSAQUE and PIXTROCO records of the TPS.INTERNAL.CONFIGS application for Inward and Outward payments.


  For PIXIN and MED Return transactions, if the debit account is configured in the `TPS.INTERNAL.CONFIGS` application, the system overrides the debit account defined in the PAYMENT.ORDER application.

## Enabling PIX Instant Payments

The user must perform the following configurations to enable the PIX Instant Payment functionality.

1. Go to **Admin Menu** > **Payments** > **Payment Hub** > **Bank System Administration** > **Programs Per weight**.


2. Set specific weight code as POT for the following records with skipindicator as Y in `PP.PROGRAMS.PER.WEIGHT` table.

   The components below are bank-specific configurations. If the bank can exclude any of the listed components, if required.

   Print.L



   Autoform.L



   BalanceCheckWithChg.L



   BankConditions.L



   Confirmations.L



   FeeDeterminationService.L



   Print.L



   Autoform.L



   Slide 1

   Slide 2

   Slide 3

   Slide 4

   Slide 5

   Slide 6

   Previous SlideNext Slide

   If the bank requires additional components to be executed for MED Return and Return Request payments or for Saque/Troco payments, the *SpecificWeightCode* should be updated in the PP.SPECIFIC.WEIGHT table. The corresponding component values must also be configured in PP.PROGRAMS.PER.WEIGHT. The screen belows shows a sample example for MED return payments.


3. For Intra bank payments, go to **Admin Menu** > **Payments** > **Payment Hub** > **Bank System Administration** > **Balance Check** > **Funds Reservation Required** (which is `PP.BALANCE.CHECK.REQUIRED` table) and set *Balancecheckreqflag* to N ..


4. Go to **Payments** > **Payment Hub** > **Bank System Administration** > **Posting Scheme** > **Statement Formats** (which is `PPT.STATEMENTFORMAT` table) and perform the following statement entry configuration as given below .


5. Go to **Payments** > **Payment Hub** > **Bank System Administration** > **Posting Scheme** and configure the `PPL.POSTINGSET` table as given below.



   DBT\_ACT and CDT\_ACT token configurations are updated for PIXINTRA payments. Apply the the same configuration for any PIX transactions.
6. Set the *Type* field in `OVERRIDE` records is updated with ERROR.



   A placeholder override has been included so ensure that all transaction-specific overrides are converted to Error.
7. For PIX future transactions, add the channel in `OVERRIDE` table to accept override automatically.



   The same configuration can be performed using an API.



   A placeholder channel has been included so the bank can configure the required channel as per their business needs.

In this topic

- [Configuring PIX Instant Payments](#ConfiguringPIXInstantPayments)

- [Pre-Configuration](#PreConfiguration)
- [Enabling PIX Instant Payments](#EnablingPIXInstantPayments)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:11:08 PM IST