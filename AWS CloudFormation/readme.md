<p align="center"><img src="https://github.com/hnawaz007/pythondataanalysis/blob/main/img/Cloudformation.jpg" alt="CloudFormation"  height="200" /></p>

<h4 align="center"> AWS CloudFormation </h1>
<p align="center">
  <a href="https://www.youtube.com/watch?v=3nsLNAZ9Zok">YouTube</a>
</p>

## CloudFormation Overview

AWS CloudFormation lets you model, provision, and manage AWS and third-party resources by treating infrastructure as code.

## Important Consideration 
In this example, we demonstrate how to create a AWS Redshift stack.  
You will need to make one change to this template. You will need to supply your public IP address under the RSIngress1 rule.  
Set the CidrIp: to your public IP address.  
```YAML
RSIngress1:  
    Type: 'AWS::EC2::SecurityGroupIngress'  
    DependsOn: RSSecurityGroup  
    Properties:  
      CidrIp: 000.00.000.000/32
```
