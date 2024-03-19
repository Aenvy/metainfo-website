#!/bin/bash

set -e

remove_images() {
  local image_regex=$1
  local have_images=$(docker images -q "${image_regex}")

  if [[ -n ${have_images} ]]; then
    docker rmi ${have_images}
    printf "Removed ${image_regex} images.\n\n"
  else
    printf "No ${image_regex} images to remove !\n\n"
  fi
}

set -x

remove_images "mc5g-metainfo-*"
