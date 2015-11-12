#!/usr/bin/env cwl-runner
class: Workflow
cwlVersion: "cwl:draft-3.dev2"

inputs:
    - { id: file1, type: File }

outputs:
    - { id: count_output, type: int, source: "#step2/parseInt_output"}

steps:
  - id: step1
    inputs:
      - { id: wc_file1, source: "#file1" }
    outputs:
      - { id: wc_output }
    run:
      id: wc
      class: CommandLineTool
      inputs:
        - { id: wc_file1, type: File, inputBinding: {} }
      outputs:
        - { id: wc_output, type: File, outputBinding: { glob: output.txt } }
      stdout: output.txt
      baseCommand: wc

  - id: step2
    inputs:
      - { id: parseInt_file1, source: "#step1/wc_output" }
    outputs:
      - { id: parseInt_output }
    run:
      class: ExpressionTool
      expression: ${return {'parseInt_output': parseInt($job.parseInt_file1.contents)};}
